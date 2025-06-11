from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_list(request):
    posts = Post.objects.order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)