# app/shop/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.shop.views import home_view, product_list_view

# namespace
app_name = 'shop'

urlpatterns = [
    path('', home_view, name='home'),
    path('product-list', product_list_view, name='product_list'),
]
