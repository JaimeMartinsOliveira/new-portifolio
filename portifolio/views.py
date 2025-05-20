from django.shortcuts import render
from .models import Experience

def home(request):
    experiencias = Experience.objects.all()
    return render(request, 'index.html', {'experiencias': experiencias})

from .models import BlogPost

def blog(request):
    posts = BlogPost.objects.all().order_by('-data_publicacao')
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})