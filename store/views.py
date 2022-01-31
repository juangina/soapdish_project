from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import * 
from .utils import cartData, guestOrder, userCartData, guestCartData, getAccessToken, quantity_choices
from .forms import ReviewForm
import json
from datetime import datetime

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
	order = data['order']
	items = data['items']
	#print(data)
	#print(cartItems, order, items)

	
	products = Product.objects.order_by('name')

	quantity_choice_available = {}
	for product in products:
		#print(product)
		product_items = product.orderitem_set.all().filter(order=order)
		#print(product_items)
		if(product_items):
			for product_item in product_items:
				#print(product_item.product.id, product_item.quantity)
				quantity_choice_available[product_item.product.id]=product.stock - product_item.quantity
				product.quantity_available = product.stock - product_item.quantity
		else:
			#print(product.id, type(product.id), 0)
			quantity_choice_available[product.id]=product.stock
			product.quantity_available = product.stock
	#print(quantity_choice_available)
	#print(quantity_choice_available[15])

	context = {
		'products':products, 
		'cartItems':cartItems,
		'quantity_choice_available': quantity_choice_available,
	}
	return render(request, 'store/store.html', context)

#Renders product page
@login_required(login_url="login")
def product(request, product_id):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	#print(data)
	#print(cartItems, order, items)

	product_item_count = 0
	for item in items:
		if item.product.id == product_id:
			product_item_count =+ item.quantity
	#print(product_item_count)

	product = get_object_or_404(Product, pk=product_id)
	reviews = product.review_set.all().order_by('created')
	
	#print(product.reviewers, request.user.customer.id)

	#print(request.user.customer.email, product.bar.creator.email)

	#print(product)
	#form = ReviewForm()
	#print(form)
	
	qty_available = product.stock-product_item_count
	quantity_choices_available = {}
	for key, value in quantity_choices.items():
		quantity_choices_available[key]=value
		#print(quantity_choices_available)
		if str(qty_available) == key:
			break

	if request.method == 'POST':
		#form = ReviewForm(request.POST)
		#review = form.save(commit=False)
		if request.POST['vote']:
			review = Review()
			review.vote = request.POST['vote']
			review.review = request.POST['review']
			review.product = product
			review.customer = request.user.customer
			review.save()
		else:
			messages.success(request, 'Please vote to leave a review')
			
			return redirect('product', product_id=product_id)

		product.getVoteCount

		messages.success(request, 'Your review was successfully submitted!')

		return redirect('product', product_id=product_id)		

	#product.getVoteCount

	context = {
        'product': product,
		#'form': form,
		'reviews': reviews,
        'cartItems': cartItems,
		'quantity_choices_available': quantity_choices_available,
		'qty_available': qty_available        
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
	#print(items)

	quantity_choices_items = {}
	quantity_choices_available = {}
	for item in items:
		#print(item.id, item.product)
		quantity_choices_items[str(item.product.id)]=quantity_choices_available
	# print(quantity_choices_items)

	for key1, value1 in quantity_choices_items.items():
		product = get_object_or_404(Product, pk=key1)
		#print(product, product.stock, value1)
		for key2, value2 in quantity_choices.items():
			# print(key1, value1, key2, value2, product.stock)
			quantity_choices_items[key1] = dict(quantity_choices_items[key1],**{key2:value2})
			if str(product.stock) == key2:
				break
		#print(quantity_choices_items)
	items = items.order_by('product')

	context = {
		'items':items, 
		'order':order, 
		'cartItems':cartItems,
		'quantity_choices': quantity_choices,
		'quantity_choices_items': quantity_choices_items,       
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
	if(cartItems <= 0):
		return redirect('cart')

	order = data['order']
	items = data['items']

	addresses = order.customer.shippingaddress_set.all()
	#print(addresses)
	#print(order)
	#print(order.id)
	previous_address = {}
	for address in addresses:
		if(address):
			previous_address['address'] = address.address
			previous_address['city'] = address.city
			previous_address['state'] = address.state
			previous_address['zipcode'] = address.zipcode
			break	
	#print(previous_address)

	allOrders = Order.objects.all()
	previousOrder = False
	for allOrder in allOrders:
		if allOrder.customer.id == request.user.id and allOrder.complete == True:
			previousOrder = True
			break
	try:
		discount = Discount.objects.get(customer=order.customer)
	except Discount.DoesNotExist:
		discount = Discount.objects.create(customer=order.customer, startDate=datetime(2022,1,1), stopDate=datetime(2022,12,31), discountActive=True)
	#discount = Discount.objects.get(customer=order.customer)
	
	context = {
		'items':items, 
		'order':order,
		'discount': discount, 
		'cartItems':cartItems,
		'address':previous_address,
		'previousOrder':previousOrder, 
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
	#print(order)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	#print(data)
	#print(orderItem)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + int(qty))
		#product.updateStock(int(qty))
		#print(product.stock, product.instock)
	elif action == 'add1':
		orderItem.quantity = (orderItem.quantity + 1)
		#product.updateStock(1)
		#print(product.stock, product.instock)
	elif action == 'remove1' and orderItem.quantity > 1:
		orderItem.quantity = (orderItem.quantity - 1)
		#product.updateStock(-1)
		#print(product.stock, product.instock)
	elif action == 'set':
		orderItem.quantity = int(qty)
		#product.updateStock(int(qty))
		#print(product.stock, product.instock)
	orderItem.save()

	if action == 'delete' or orderItem.quantity <= 0:
		#product.updateStock(-orderItem.quantity)
		#print(product.stock, product.instock)
		orderItem.delete()
		return JsonResponse('Item was deleted', safe=False)

	return JsonResponse('Item(s) was added', safe=False)

@login_required(login_url="login")
def getTotal(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	total = order.get_checkout_total
	return JsonResponse({'total': total}, safe=False)

@login_required(login_url="login")
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	#print(data)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_checkout_total:
		order.complete = True
		order.total_cost = order.get_checkout_total
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['billing']['address'],
		city=data['billing']['city'],
		state=data['billing']['state'],
		zipcode=data['billing']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

#Renders paypal api checkout page 
@login_required(login_url='login')
def apiCheckout(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	accessToken = getAccessToken(request)
	context = {
		'payPalAPI': "Paypal Server Side Integration",
		'accessToken': accessToken,
		'cartItems':cartItems
	}
	return render(request, 'store/api_checkout.html', context)


