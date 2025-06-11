from django.urls import path
from .views import register_view

urlpatterns = [
    path('register-view/', register_view, name='register_view'),
]