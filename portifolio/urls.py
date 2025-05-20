from django.urls import path, include
from .views import home, blog, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', post_detail, name='post_detail'),
]