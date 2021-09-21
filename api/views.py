from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import BarSerializer, CreatorSerializer, Conversation_MetaSerializer, Conversation_DialogSerializer, ContactSerializer,CustomerSerializer,ProductSerializer,OrderSerializer,OrderItemSerializer,ShippingAddressSerializer

from django.contrib.auth.models import User, Group
from bars.models import Bar
from chatbot.models import Conversation_Meta, Conversation_Dialog
from contacts.models import Contact
from creators.models import Creator
from store.models import Customer, Product, Order, OrderItem, ShippingAddress

from datetime import datetime

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













