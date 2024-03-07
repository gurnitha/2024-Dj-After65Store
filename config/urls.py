# config/urls.py

# Django dan third party modules
from django.contrib import admin
from django.urls import path, include  


urlpatterns = [

    # admin path 
    path("admin/", admin.site.urls),

    # shop path
    path('', include('app.shop.urls', namespace='shop')),

    # blog path
    path('', include('app.blog.urls', namespace='blog')),
]
