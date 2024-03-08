# app/shop/views.py

# Django dan third party modules
from django.shortcuts import render


def home_view(request):

	# data
	page_title 	= 'After65Shop'
	customer 	= 'Ujang'

	context_dictionary = {
		'page_title':page_title,
		'customer':customer
	}
	
	return render(request, 'shop/index.html', context_dictionary)


def product_list_view(request):

	return render(request, 'shop/product_list.html')


def wishlist_view(request):

	return render(request, 'shop/wishlist.html')


def cart_view(request):

	return render(request, 'shop/cart.html')


def checkout_view(request):

	return render(request, 'shop/checkout.html')