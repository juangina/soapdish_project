from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from store.utils import cookieCart, cartData, guestOrder

def login(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'cartItems': cartItems
    } 
    return render(request, 'accounts/login.html', context)

def register(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'cartItems': cartItems
    }     
    return render(request, 'accounts/register.html', context)

def logout(request):   
    return redirect('index')

def dashboard(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'cartItems': cartItems
    }        
    return render(request, 'accounts/dashboard.html', context)


