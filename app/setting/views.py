# app/setting/views.py

# Django dan third party modules
from django.shortcuts import render


def setting_data_statis_view(request):

	page_title 		= 'Test Page Title'
	phone_number	= '(+62) xxxx-xxxx-xxxx'

	data_statis 	= {
		'page_title':page_title,
		'phone_number':phone_number,
	}

	return render(request, 'setting/setting_data_statis.html', data_statis)