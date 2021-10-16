from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from store.utils import cartData
from django.contrib.auth.decorators import login_required

category_choices = {
  'expenses':'Expenses',
  'equipment':'Equipment',
  'supplies':'Supplies',
  'consumables': 'Consumables',
  'materials':'Materials',
  'stock':'Stock',
  }

#Renders product listing page
@login_required(login_url="inventory")
def inventory(request):
	data = cartData(request)
	cartItems = data['cartItems']
	
	category = ''	
	name = ''
	keywords = ''
	expenses_sum = 0
	inventory_sum = 0


    # Search for Category in category
	if 'category' in request.GET:
		category = request.GET['category']
		if category == 'expenses':
			queryset_list = Expenses.objects.all().order_by('purchase_date')
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
		else:
			queryset_list = Inventory.objects.all()
			queryset_list = queryset_list.filter(name__category__iexact=category)
			inventory_sum = sum([item.name.unit_price for item in queryset_list])

	context = {
		'cartItems': cartItems,
		'category_choices': category_choices,
		'values': request.GET,
		'category': category,
		'inventory': queryset_list, 
		'expenses_sum': expenses_sum,
		'inventory_sum': inventory_sum,
	}
	return render(request, 'inventory/inventory.html', context)

