from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-posts', views.all_posts, name='all-posts'),
    path('posts/add', views.add_post, name='add-posts'),
    path('posts/<int:id>/edit', views.edit_post, name='adjust-posts'),
    path('posts/<int:id>/delete', views.delete_post, name='delete-posts'),
    path('posts/<int:id>', views.post_detail, name='post-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)