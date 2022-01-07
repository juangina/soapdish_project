from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('orders/', views.customer_orders, name='customer_orders'),
    path('orders/<order_id>', views.customer_order, name='customer_order')
]