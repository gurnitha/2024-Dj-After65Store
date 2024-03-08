# app/account/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.account.views import register_login_view

# namespace
app_name = 'account'

urlpatterns = [
    path('register-login/', register_login_view, name='register_login'),
]
