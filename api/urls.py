from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    
    path('bars/', views.getBars),
    path('bars/add/', views.addBar),
    path('bars/<str:pk>/', views.getBar),


    #Paypal Server Side Integration Endpoints
	path('order/token', views.getToken, name="get_token"),
	path('order/<order_id>/view', views.viewOrder, name="view_order"),
	path('order/<approve_link>/<order_id>/approve', views.approveOrder, name="approve_order"),

	path('order/create', views.createOrder, name="create_order"),
	path('order/<order_id>/capture/', views.captureOrder, name="capture_order"),
]