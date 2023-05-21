from rest_framework import serializers

from django.contrib.auth.models import User, Group
from creators.models import Creator
from bars.models import Bar
from contacts.models import Contact
from store.models import Customer, Product, Order, OrderItem, ShippingAddress

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BarSerializer(serializers.ModelSerializer):
    #Override the owner attribute that is being serialized in the class Meta model
    creator = CreatorSerializer(many=False)
    products = serializers.SerializerMethodField()

    class Meta:
        model = Bar
        fields = '__all__'

    #The obj being passed in is Bar, the one referenced by the Foreign Key
    def get_products(self, obj):
        products = obj.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return serializer.data




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'




class Conversation_MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation_Meta
        fields = '__all__'

class Conversation_DialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation_Dialog
        fields = '__all__'


