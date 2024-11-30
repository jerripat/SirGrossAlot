from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post




def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]  # Get the latest three posts
    return render(request, 'blog/templates/blog/index.html', {'posts': latest_posts})


def posts(request):
    all_posts  = Post.objects.all().order_by('-date')  # Get all posts in descending order of date
    return render(request, 'blog/templates/blog/all-posts.html', {'all_posts': all_posts})

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)  # Try to find the post with the given slug
    return render(request, 'blog/templates/blog/post-detail.html', {
        'post': identified_post
    })