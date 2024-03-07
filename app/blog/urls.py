# app/blog/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.blog.views import post_list_view

# namespace
app_name = 'blog'

urlpatterns = [
    path('post-list/', post_list_view, name='post_list'),
]
