# app/shop/views.py

# Django dan third party modules
from django.shortcuts import render


def home_view(request):
	return render(request, 'shop/index.html')