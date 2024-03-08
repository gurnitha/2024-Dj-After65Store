# app/setting/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.setting.views import setting_data_statis_view

# namespace
app_name = 'setting'

urlpatterns = [
    path('setting/', setting_data_statis_view, name='setting_data_statis'),
]
