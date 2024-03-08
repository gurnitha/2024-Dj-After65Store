# app/setting/views.py

# Django dan third party modules
from django.shortcuts import render


def about_view(request):

	return render(request, 'setting/about.html')


def contact_view(request):

	return render(request, 'setting/contact.html')