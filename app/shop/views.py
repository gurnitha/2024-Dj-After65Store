# app/shop/views.py

# Django dan third party modules
from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
	return HttpResponse('<h1>Hallo World</h1><br><p>Selamat datang di After65Shop</p>')