# app/setting/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.setting.views import about_view, contact_view

# namespace
app_name = 'setting'


urlpatterns = [
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]