from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-date')
    return render(request, 'blog/index.html', {'posts': latest_posts})

def all_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detailed-posts.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        date = request.POST.get('date')

        # Validate fields
        if not all([title, location, description, image, date]):
            message = 'All fields are required'
            return render(request, 'blog/add-posts.html', {'message': message})

        # Create a new post linked to the logged-in owner
        post = Post(
            title=title,
            location=location,
            description=description,
            image=image,
            date=date
        )
        post.save()
        message = 'Post added successfully'
        return render(request, 'blog/add-posts.html', {'message': message})

    return render(request, 'blog/add-posts.html')

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        message = 'Post deleted successfully'
        return render(request, 'blog/index.html', {'post': post, 'message': message})
    else:
        message = 'You can not delete this post'
        return render(request, 'blog/delete-posts.html', {'post': post, 'message': message})

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.location = request.POST.get('location')
        post.description = request.POST.get('description')
        post.image = request.FILES.get('image')
        post.date = request.POST.get('date')
        post.save()
        message = 'Post updated successfully'
        return render(request, 'blog/adjust-posts.html', {'post': post, 'message': message})
    else:
        message = 'You can not edit the post details'
        return render(request, 'blog/adjust-posts.html', {'post': post, 'message': message})
