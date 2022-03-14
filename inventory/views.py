from django.db.models import query
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from store.utils import cartData
from django.contrib.auth.decorators import login_required
from django.db.models import Q

category_choices = {
	'': 'All',
  'ingredient':'Ingredients',
  'packaging': 'Packaging',
  'equipment':'Equipment',
  'supplies':'Supplies',
  'training': 'Training',
  'subscription':'Subscription',
  'advertising': 'Advertising',
  'office': 'Office',
  'transportation': 'Transportation',
  'finance': 'Finance Charges',
  'legal': 'Legal',
  'shipping': 'Shipping',
  'taxes': 'Taxes'
  }

#Renders product listing page
@login_required(login_url="expenses")
def expenses(request):
	if not request.user.is_superuser:
		return redirect('login')
	data = cartData(request)
	cartItems = data['cartItems']
	
	category = ''	
	name = ''
	keywords = ''
	expenses_sum = 0
	queryset_list = ''

	queryset_list = Expenses.objects.all().order_by('purchase_date')
    # Search for Category in category
	if 'category' in request.GET:
		category = request.GET['category']
		if category:
			queryset_list = queryset_list.filter(category__icontains=category)
	# Search for Name in name
	if 'name' in request.GET:
		name = request.GET['name']
		if name:
			queryset_list = queryset_list.filter(name__icontains=name)
		# Search for Keywords in description	
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)
	expenses_sum = sum([(item.unit_price * item.quantity) for item in queryset_list])

	context = {
		'cartItems': cartItems,
		'category_choices': category_choices,
		'values': request.GET,
		'category': category,
		'inventory': queryset_list, 
		'expenses_sum': expenses_sum,
	}
	return render(request, 'inventory/expenses.html', context)

@login_required(login_url="inventory")
def inventory(request):
	if not request.user.is_superuser:
		return redirect('login')
	data = cartData(request)
	cartItems = data['cartItems']
	
	category = ''	
	name = ''
	keywords = ''
	inventory_sum = 0
	queryset_list = ''

	queryset_list = Inventory.objects.all().order_by('bar_soap__created_date')

    # Search for Hand Soap and Bath Soap in Name
	lookups = (Q(name__name__icontains="Hand Soap") | Q(name__name__icontains="Bath Soap"))

	#queryset_list = queryset_list.filter(name__name__icontains="Hand Soap")
	queryset_list = queryset_list.filter(lookups)

	inventory_sum = sum([(item.bar_soap.price * item.quantity_available) for item in queryset_list])

	context = {
		'cartItems': cartItems,
		'inventory': queryset_list,
		'inventory_sum': inventory_sum, 
	}
	return render(request, 'inventory/inventory.html', context)

