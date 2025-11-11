from datetime import date
from django.shortcuts import render
from .models import Post


#all_posts = [     

    #{
    #    "slug": "hike-in-the-mountains",
    #    "image": "mountain.png",
    #    "author": "Diana",
    #    "date": date(2025, 2, 16),
    #    "title": "Mountain Hiking",
    #    "excerpt": "There is nothing like the views you get when hiking in the mountains! And I was not prepared for what happened whilst I was enjoying the view!",
    #    "content": "This is a big mountain!"
    #},
    #{
    #    "slug": "exploring-the-forest",
    #    "image": "forest.png",
    #    "author": "John",
    #   "date": date(2025, 1, 10),
    #    "title": "Exploring the Deep Forest",
    #    "excerpt": "The forest is full of mysteries! I had no idea what I would find when I wandered deeper...",
    #    "content": "The trees were tall, and the air was fresh..."
    #},
    #{
    #    "slug": "beach-walk-at-sunset",
    #    "image": "beach.png",
    #    "author": "Emily",
    #    "date": date(2024, 12, 5),
    #    "title": "Beach Walk at Sunset",
    #    "excerpt": "Walking on the beach at sunset is a magical experience. The sky was painted in beautiful colors!",
    #    "content": "The waves were crashing gently as the sun dipped below the horizon..."
    #}
#]

def starting_page(request):
    #sorted_posts = sorted(all_posts, key=lambda post: post["date"], reverse=True)  # Sort newest to oldest
    #latest_posts = sorted_posts[:3]  # Get the 3 most recent posts

    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    post = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": post
    })

    #return render (request, "blog/all-posts.html")


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/detailed-posts.html", {
        "post": post,
        "post_tags": post.tags.all()
    })
    
    
    #return render (request, "blog/detailed-posts.html")
