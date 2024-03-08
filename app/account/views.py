# app/account/views.py

# Django dan third party modules
from django.shortcuts import render


def register_login_view(request):

	return render(request, 'account/register_login.html')