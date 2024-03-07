# app/blog/views.py

# Django dan third party modules
from django.shortcuts import render


def post_list_view(request):

	return render(request, 'blog/post_list.html')


def post_details_view(request):

	return render(request, 'blog/post_details.html')