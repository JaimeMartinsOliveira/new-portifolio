# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),
    path('post/<slug:slug>/', views.blog_detail, name='detail'),
]