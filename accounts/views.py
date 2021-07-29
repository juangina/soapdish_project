from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

from store.models import Customer
from store.utils import cookieCart, cartData, guestOrder

def register(request):
    if request.method == 'POST':
        #Testing the Messaging system
        messages.error(request, 'Testing error message')
        return redirect('register')

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Server Side Authentication Passed
                    # register User
                    user = User.objects.create_user (first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    # Login after registering
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    #user.save();
                    customer = Customer.objects.create(user = user, name= first_name + ' ' + last_name, email=email)
                    customer.save();
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        context = {
            'cartItems': cartItems
        }     
        return render(request, 'accounts/register.html', context)

def login(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Login after registering
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid creditials')
            return render(request, 'accounts/login.html')
    else:
        context = {
            'cartItems': cartItems
        } 
        return render(request, 'accounts/login.html', context)

def dashboard(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'cartItems': cartItems
    }        
    return render(request, 'accounts/dashboard.html', context)

def logout(request):   
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    else:
        return redirect('index')



