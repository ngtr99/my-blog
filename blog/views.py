from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .supabase_storage import upload_image_to_supabase


def index(request):
    latest_posts = Post.objects.order_by("-date")
    return render(request, "blog/index.html", {"posts": latest_posts})


def all_posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/detailed-posts.html", {"post": post})


def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        raw_date = request.POST.get("date")

        if not all([title, location, description, image, raw_date]):
            return render(
                request,
                "blog/add-posts.html",
                {"message": "All fields are required"},
            )

        try:
            parsed_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
            image_url = upload_image_to_supabase(image)

            post = Post(
                title=title,
                location=location,
                description=description,
                image_url=image_url,
                date=parsed_date,
            )
            post.save()

            return render(
                request,
                "blog/add-posts.html",
                {"message": "Post added successfully"},
            )
        except Exception as e:
            return render(
                request,
                "blog/add-posts.html",
                {"message": f"Error adding post: {e}"},
            )

    return render(request, "blog/add-posts.html")


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()
        return redirect("all-posts")

    return render(
        request,
        "blog/delete-posts.html",
        {"post": post, "message": "You can not delete this post"},
    )


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        try:
            post.title = request.POST.get("title")
            post.location = request.POST.get("location")
            post.description = request.POST.get("description")

            raw_date = request.POST.get("date")
            if raw_date:
                post.date = datetime.strptime(raw_date, "%Y-%m-%d").date()

            new_image = request.FILES.get("image")
            if new_image:
                post.image_url = upload_image_to_supabase(new_image)

            post.save()

            return render(
                request,
                "blog/adjust-posts.html",
                {"post": post, "message": "Post updated successfully"},
            )
        except Exception as e:
            return render(
                request,
                "blog/adjust-posts.html",
                {"post": post, "message": f"Error updating post: {e}"},
            )

    return render(
        request,
        "blog/adjust-posts.html",
        {"post": post},
    )
    
    