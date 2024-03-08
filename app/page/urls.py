# app/page/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.page.views import about_view, contact_view

# namespace
app_name = 'page'


urlpatterns = [
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]