from django.shortcuts import render, get_object_or_404
# Se o seu modelo se chamar Post, mantenha. Se for BlogPost, altere aqui.
from .models import Post

def blog_list(request):
    posts = Post.objects.order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context)
