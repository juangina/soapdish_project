from django.urls import path

from . import views

urlpatterns = [
	#Render Page Endpoints
	#Leave as empty string for base url
	path('', views.inventory, name="inventory"),
	# path('<int:product_id>', views.product, name="product"),
	# path('cart/', views.cart, name="cart"),
	# path('checkout/', views.checkout, name="checkout"),
	
	#API Endpoints - Updates values in the database
	#JS on the Front End redirects/reloads the web page
	#The page is updated based on the updated database
	# path('update_item/', views.updateItem, name="update_item"),
	# path('process_order/', views.processOrder, name="process_order"),
]