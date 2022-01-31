from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.deletion import CASCADE
from bars.models import Bar
from decimal import Decimal
import uuid
from datetime import datetime

# from django.db.models.signals import post_save
# from django.dispatch import receiver

#set a default bar for product if assigned bar is deleted
def get_deleted_bar():
	return Bar.objects.get_or_create(name='delected')[0]

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name

class Product(models.Model):

	quantity_available = 0

	name = models.CharField(max_length=200, blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	bar = models.ForeignKey(Bar, default=None, on_delete=models.SET(get_deleted_bar), blank=True)
	stock = models.IntegerField(default=0, null=True, blank=True)
	instock = models.BooleanField(default=False, null=True, blank=True)
	vote_total = models.IntegerField(default=0, null=True, blank=True)
	vote_ratio = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	def updateStock(self, quantity):
		self.stock -= quantity
		if(self.stock) >= 0:
			self.instock == True
		else:
			self.instock == False
		self.save() 
		return self.stock
	
	@property
	def reviewers(self):
		queryset = self.review_set.all().values_list('customer__id', flat=True)
		return queryset
		
	@property
	def getVoteCount(self):
		reviews = self.review_set.all()
		#print(reviews)
		upVotes = reviews.filter(vote='up').count()
		totalVotes = reviews.count()
		ratio = (upVotes / totalVotes) * 100
		self.vote_total = totalVotes
		self.vote_ratio = ratio
		self.save()

class SpecialFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_tip = models.TextField(null=True, blank=True)
    key_ingredients = models.CharField(max_length=200, blank=True, null=True)
    key_benefits = models.CharField(max_length=200, blank=True, null=True)
    suitable_for = models.CharField(max_length=200, blank=True, null=True)
    for_best_results = models.CharField(max_length=200, blank=True, null=True)
    made_with = models.CharField(max_length=200, blank=True, null=True)
    smells_like = models.CharField(max_length=200, blank=True, null=True)
    notes_of = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Discount(models.Model):
	DISCOUNT_TYPES = (
        ('FTB2022', 'First Time Buyer'),
        ('WAF2022', 'We Are Family'),
		('FRB2022', 'Frequent Buyer'),
		('LYS2022', 'Loyal Subscriber'),
    )
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
	discountType = models.CharField(max_length=200, default='FTB2022')
	discountActive = models.BooleanField(default=False)
	startDate = models.DateTimeField()
	stopDate = models.DateTimeField()
	ftbDiscountBalance = models.DecimalField(max_digits=5, decimal_places=2, default=4.50)
	wafDiscountBalance = models.DecimalField(max_digits=5, decimal_places=2, default=4.50)
	frbDiscountBalance = models.DecimalField(max_digits=5, decimal_places=2, default=4.50)
	lysDiscountBalance = models.DecimalField(max_digits=5, decimal_places=2, default=4.50)
	id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
	def __str__(self):
		return self.discountType

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	transaction_id = models.CharField(max_length=100, null=True)
	shipping_cost = models.DecimalField(max_digits=5, decimal_places=2, default=7.50)
	total_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	complete = models.BooleanField(default=False)


	def __str__(self):
		return str(self.id)
		
	@property
	def get_items(self):
		orderitems = self.orderitem_set.all()
		return orderitems

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_checkout_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		
		orders = Order.objects.all()
		previousOrder = False
		for order in orders:
			if order.customer.id == self.customer.id and order.complete == True:
				previousOrder = True
				break
		if previousOrder == True:
			return self.shipping_cost + total
		else:
			try:
				discount = Discount.objects.get(customer=self.customer)
			except Discount.DoesNotExist:
				discount = Discount(customer=self.customer, startDate=datetime(2022,1,1), stopDate=datetime(2022,12,31), discountActive=True)

			return self.shipping_cost + total - discount.ftbDiscountBalance

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class Review(models.Model):
	VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	review = models.TextField(null=True, blank=True)
	vote = models.CharField(max_length=200, choices=VOTE_TYPE)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
	class Meta:
		unique_together = [['customer', 'product']]
		
	def __str__(self):
		return self.vote
	
	@property
	def reviewers(self):
		queryset = self.review_set.all().values_list('customer__id', flat=True)
		return queryset
	
	@property
	def lastNameInitial(self):
		str = self.customer.user.last_name
		firstCharacter = str[:1]
		return firstCharacter













# @receiver(post_save, sender=Order)
# def createOrder(sender, instance, created, **kwargs):
# 	print(sender, instance,created)
# 	if created == True:
# 		print("Order Created")

# @receiver(post_save, sender=Order)
# def updateOrder(sender, instance, created, **kwargs):
# 	print(sender, instance,created)
# 	order = instance
# 	completed = order.complete
# 	if created == False and completed == False:
# 		print("Order Updated")

# @receiver(post_save, sender=Order)
# def completeOrder(sender, instance, created, **kwargs):
# 	print(sender, instance,created)
# 	order = instance
# 	completed = order.complete
# 	if created == False and completed == True:
# 		print("Order Completed")

#post_save.connect(createOrder, sender=Order)
#post_save.connect(updateOrder, sender=Order)
#post_save.connect(completeOrder, sender=Order