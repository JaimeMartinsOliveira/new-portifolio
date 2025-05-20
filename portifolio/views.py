from django.shortcuts import render
from .models import Experience, BlogPost, Skill, Formacao

def home(request):
    experiencias = Experience.objects.all()
    skills = Skill.objects.all()
    formacoes = Formacao.objects.all()
    return render(request, 'index.html', {
        'experiencias': experiencias,
        'skills': skills,
        'formacoes': formacoes,
    })

def blog(request):
    posts = BlogPost.objects.all().order_by('-data_publicacao')
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})