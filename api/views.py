from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import BarSerializer, CreatorSerializer, Conversation_MetaSerializer, Conversation_DialogSerializer, ContactSerializer,CustomerSerializer,ProductSerializer,OrderSerializer,OrderItemSerializer,ShippingAddressSerializer

from bars.models import Bar
from creators.models import Creator
from store.models import Customer, Product, Order, OrderItem, ShippingAddress

from datetime import datetime

import requests
import json

@login_required
def getAccessToken(request):
	url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
	headers = {
				'Authorization': 'Basic QWFGenpIc3JiS1d3Y003NTZsd0hmN3RQamlCMjhRdVl4WXcxTlQ2cFBQaVlxcWZXbWVJa1ZsVDNQQkVJZ0xKRm9RWG81UXdYNzdEZ1FjLWo6RUJyczVwSWREOEh1TkdZRU5mWWd5TzZqY2FkUEFqVU04WjZnZGZvYm1Vek9XUGM3QU1NanBFXzJkV3VKSjB2anhIUWdMdEs4Snd5Mm1tUEY=',

				'Content-Type': 'application/x-www-form-urlencoded'
				}
	payload='grant_type=client_credentials'
	response = requests.request("POST", url, headers = headers, data = payload)
	response_json = response.json()
	accessToken = response_json['access_token']
	return accessToken

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/bars'},
        {'GET': '/api/bars/id'},
        {'POST': '/api/bars'},
        
        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getBars(request):
    #print('USER: ', request.user)
    bars = Bar.objects.all()
    serializer = BarSerializer(bars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getBar(request, pk):
   bar = Bar.objects.get(id=pk)
   serializer = BarSerializer(bar, many=False)
   return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBar(request):

    #print('USER: ', request.user)
    #print('DATA: ', request.data)

    creator = Creator.objects.get(name=request.data['creator'])
    name = request.data['name']
    fragrance = request.data['fragrance']
    batch_code = request.data['batch_code']
    description = request.data['description']
    colorants = request.data['colorants']
    nutrients = request.data['nutrients']
    exfolients = request.data['exfolients']
    price = request.data['price']
    is_cured = request.data['is_cured']
    created_date = datetime.now()

    bar = Bar(creator=creator, name=name, fragrance=fragrance, batch_code=batch_code, description=description, colorants=colorants, nutrients=nutrients, exfolients=exfolients, price=price, is_cured=is_cured, created_date=created_date)
    bar.save()

    serializer = BarSerializer(bar, many=False)
    return Response(serializer.data)

#Paypal API server test views
@login_required(login_url='login')
def getToken(request):
	url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
	headers = {
				'Authorization': 'Basic QWFGenpIc3JiS1d3Y003NTZsd0hmN3RQamlCMjhRdVl4WXcxTlQ2cFBQaVlxcWZXbWVJa1ZsVDNQQkVJZ0xKRm9RWG81UXdYNzdEZ1FjLWo6RUJyczVwSWREOEh1TkdZRU5mWWd5TzZqY2FkUEFqVU04WjZnZGZvYm1Vek9XUGM3QU1NanBFXzJkV3VKSjB2anhIUWdMdEs4Snd5Mm1tUEY=',

				'Content-Type': 'application/x-www-form-urlencoded'
				}
	payload='grant_type=client_credentials'
	response = requests.request("POST", url, headers = headers, data = payload)
	response_json = response.json()
	print(response_json)

	# Authorization = "Bearer {}"
	# Authorization = Authorization.format(access_token)
	# print(Authorization)

	return JsonResponse("Paypal Token Recieved...", safe=False)

#Paypal API server integration with Paypal JS SDK 
@login_required(login_url='login')
def createOrder(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

	total = order.get_checkout_total

	accessToken = getAccessToken(request)
	url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
	payload = json.dumps({
	"intent": "CAPTURE",
	"purchase_units": [
		{
		"amount": {
			"currency_code": "USD",
			"value": total,
			}
		}
	]
	})
	headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Bearer ' + accessToken
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	response_json = response.json()
	#print(response_json)
	
	return JsonResponse(response_json, safe=False)

@login_required(login_url='login')
def viewOrder(request, order_id):
	accessToken = getAccessToken(request)
	#order_id = '8M659927918803629'
	url = "https://api.sandbox.paypal.com/v2/checkout/orders/" + order_id
	payload={}
	headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Bearer ' + accessToken,
	'Cookie': 'LANG=en_US%3BUS; cookie_check=yes; d_id=da1bff7e9149485980c0f8f91f669f4c1641477856400; enforce_policy=ccpa; ts=vreXpYrS%3D1736172255%26vteXpYrS%3D1641479655%26vr%3D2fb45a5417e0a6022c4a317dd8c31d98%26vt%3D2fb45a5417e0a6022c4a317dd8c31d97%26vtyp%3Dnew; ts_c=vr%3D2fb45a5417e0a6022c4a317dd8c31d98%26vt%3D2fb45a5417e0a6022c4a317dd8c31d97; tsrce=unifiedloginnodeweb; x-cdn=fastly:FTY; x-pp-s=eyJ0IjoiMTY0MTQ3Nzg1NjQzMSIsImwiOiIwIiwibSI6IjAifQ'
	}

	response = requests.request("GET", url, headers=headers, data=payload)
	response_json = response.json()
	#print(response_json)
	
	return JsonResponse(response_json, safe=False)

@login_required(login_url='login')
def approveOrder(request, order_id):
	url = "https://www.sandbox.paypal.com/checkoutnow?token=" + order_id

	payload={}
	headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie': 'LANG=en_US%3BUS; cookie_check=yes; d_id=da1bff7e9149485980c0f8f91f669f4c1641477856400; enforce_policy=ccpa; ts=vreXpYrS%3D1736172255%26vteXpYrS%3D1641479655%26vr%3D2fb45a5417e0a6022c4a317dd8c31d98%26vt%3D2fb45a5417e0a6022c4a317dd8c31d97%26vtyp%3Dnew; ts_c=vr%3D2fb45a5417e0a6022c4a317dd8c31d98%26vt%3D2fb45a5417e0a6022c4a317dd8c31d97; tsrce=unifiedloginnodeweb; x-cdn=fastly:FTY; x-pp-s=eyJ0IjoiMTY0MTQ3Nzg1NjQzMSIsImwiOiIwIiwibSI6IjAifQ; nsid=s%3AMvM83Uzjn2NmmNMgCckugOmqFLLuBzUT.dtSMnQ0GCDs%2ByZwfBohzVDg8OjQIQQTq6gvOwLK9PvI'
	}

	response = requests.request("GET", url, headers=headers, data=payload)
	response_json = response.json()
	print(response_json)

	return JsonResponse(response_json, safe=False)

@login_required(login_url='login')
def captureOrder(request,order_id):
	accessToken = getAccessToken(request)
	url = "https://api.sandbox.paypal.com/v2/checkout/orders/" + order_id + "/capture"

	payload = ""
	headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Bearer ' + accessToken,
	'Cookie': 'LANG=en_US%3BUS; cookie_check=yes; d_id=da1bff7e9149485980c0f8f91f669f4c1641477856400; enforce_policy=ccpa; ts=vreXpYrS%3D1736172255%26vteXpYrS%3D1641479655%26vr%3D2fb45a5417e0a6022c4a317dd8c31d98%26vt%3D2fb45a5417e0a6022c4a317dd8c31d97%26vtyp%3Dnew; ts_c=vr%3D2fb45a5417e0a6022c4a317dd8c31d98%26vt%3D2fb45a5417e0a6022c4a317dd8c31d97; tsrce=unifiedloginnodeweb; x-cdn=fastly:FTY; x-pp-s=eyJ0IjoiMTY0MTQ3Nzg1NjQzMSIsImwiOiIwIiwibSI6IjAifQ'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	response_json = response.json()
	#print(response_json)

	return JsonResponse(response_json, safe=False)














