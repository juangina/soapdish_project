from django.urls import path

from . import views

urlpatterns = [
	#Render Page Endpoints
	path('expenses', views.expenses, name="expenses"),
	path('inventory', views.inventory, name="inventory"),
]