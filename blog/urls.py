from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='list'),  # Rota com o nome 'list'
    path('post/<int:pk>/', views.blog_detail, name='detail'), # ex: /blog/post/5/
]