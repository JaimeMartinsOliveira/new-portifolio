from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'), # ex: /blog/
    path('post/<int:pk>/', views.blog_detail, name='detail'), # ex: /blog/post/5/
]