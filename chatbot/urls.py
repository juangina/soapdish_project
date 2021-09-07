from django.urls import path

from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.index, name='home'),
    path('api/chatbot/', views.ChatBotApiView.as_view(), name='chatbot'),

]