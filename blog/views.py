import markdown2
from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_list(request):
    posts = Post.objects.order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    content_html = markdown2.markdown(post.content)

    context = {
        'post': post,
        'content_html': content_html,
    }
    return render(request, 'blog/blog_detail.html', context)
