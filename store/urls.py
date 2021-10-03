from django.urls import path

from . import views

urlpatterns = [
	#Render Page Endpoints
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('<int:product_id>', views.product, name="product"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	
	#API Endpoints
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]
