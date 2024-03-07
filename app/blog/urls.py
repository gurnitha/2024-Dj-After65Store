# app/blog/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.blog.views import post_list_view, post_details_view

# namespace
app_name = 'blog'

urlpatterns = [
    path('post-list/', post_list_view, name='post_list'),
    path('post-details/1/', post_details_view, name='post_details'),
]
