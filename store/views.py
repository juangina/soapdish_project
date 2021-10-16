from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cartData, guestOrder, userCartData, guestCartData, quantity_choices
from django.contrib.auth.decorators import login_required

# from django import template
# register = template.Library()

# @register.simple_tag
# def quote(str):
#     return f'"{str}"'

#Renders product listing page
@login_required(login_url="login")
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']

	products = Product.objects.all()
	context = {
		'products':products, 
		'cartItems':cartItems,
	}
	return render(request, 'store/store.html', context)

#Renders product page
@login_required(login_url="login")
def product(request, product_id):
    data = cartData(request)
    cartItems = data['cartItems']
    
    #product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'cartItems': cartItems,
		'quantity_choices': quantity_choices        
    }
    return render(request, 'store/product.html', context)

#Renders cart page
@login_required(login_url="login")
def cart(request):
	if request.user.is_authenticated:
		data = userCartData(request)
	else:
		data = guestCartData(request)

	#data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {
		'items':items, 
		'order':order, 
		'cartItems':cartItems,
		'quantity_choices': quantity_choices       
	}
	return render(request, 'store/cart.html', context)

#Renders checkout page 
@login_required(login_url="login")
def checkout(request):
	if request.user.is_authenticated:
		data = userCartData(request)
	else:
		data = guestCartData(request)

	#data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {
		'items':items, 
		'order':order, 
		'cartItems':cartItems 
	}
	return render(request, 'store/checkout.html', context)


#API - Return updated cart quantity status Json data
@login_required(login_url="login")
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	qty = data['qty']
	#print('Action:', action)
	#print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	#print(data)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + int(qty))
	elif action == 'add1':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove1' and orderItem.quantity > 1:
		orderItem.quantity = (orderItem.quantity - 1)
	elif action == 'set':
		orderItem.quantity = int(qty)

	orderItem.save()

	if action == 'delete' or orderItem.quantity <= 0:
		orderItem.delete()
		return JsonResponse('Item was deleted', safe=False)

	return JsonResponse('Item(s) was added', safe=False)

#API - Returns 
@login_required(login_url="login")
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
