import os
import uuid
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
BUCKET_NAME = "post-images"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def upload_image_to_supabase(file_obj) -> str:
    ext = ""
    if "." in file_obj.name:
        ext = "." + file_obj.name.rsplit(".", 1)[1].lower()

    filename = f"posts/{uuid.uuid4().hex}{ext}"
    content = file_obj.read()

    supabase.storage.from_(BUCKET_NAME).upload(
        path=filename,
        file=content,
        file_options={
            "content-type": file_obj.content_type or "application/octet-stream",
            "upsert": "false",
        },
    )

    public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(filename)
    return public_url