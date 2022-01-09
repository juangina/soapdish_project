from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from requests import check_compatibility
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

from store.models import Customer, Order, OrderItem, ShippingAddress, Product
from store.utils import cookieCart, cartData, guestOrder

def register(request):
    if request.method == 'POST':
        #Testing the Messaging system
        #messages.error(request, 'Testing error message')
        #return redirect('register')

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        username = username.lower()
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check if username already taken
            # Backwards logic
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken.')
                return redirect('register')
            else:
                # Checks if email already taken
                # Backwards logic
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used.')
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
                    customer.save()

                    #messages.success(request, 'You are now registered and can log in.')
                    auth.login(request, user)
                    messages.success(request, 'You are now registered and log in.')

                    return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match.')
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
    if request.user.is_authenticated:
        return redirect('dashboard')

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
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        context = {
            'cartItems': cartItems
        } 
        return render(request, 'accounts/login.html', context)

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']

        user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
        context = {
            'cartItems': cartItems,
            'contacts': user_contacts
        }        
        return render(request, 'accounts/dashboard.html', context)
    else:
        messages.error(request, 'Please login to gain access to dashboard.')
        return redirect ('login')

@login_required
def orders(request):
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        customer = get_object_or_404(Customer, user=request.user)
        customer_orders = customer.order_set.all().order_by('-date_ordered').filter(complete=True)
        context = {
            'cartItems': cartItems,
            'customer_orders': customer_orders
        }        
        return render(request, 'accounts/orders.html', context)
    else:
        messages.error(request, 'Please login to gain access to dashboard.')
        return redirect ('login')

@login_required
def order(request, order_id):
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        order = Order.objects.get(pk=order_id)
        order_items = order.orderitem_set.all().order_by('-product')
        context = {
            'cartItems': cartItems,
            'order_items': order_items
        }        
        return render(request, 'accounts/order.html', context)
    else:
        messages.error(request, 'Please login to gain access to dashboard.')
        return redirect ('login')

@login_required
def logout(request):   
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    else:
        return redirect('index')

@login_required
def contactinfo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Get email form values
            email = request.POST['email']
            email2 = request.POST['email2']
            if email == email2:
                # Get remaining form values
                name = request.POST['name']
                #address = request.POST['address']
                #city = request.POST['city']
                #state = request.POST['state']
                #zipcode = request.POST['zipcode']
                customer = Customer.objects.get(user = request.user)
                customer.name = name
                customer.email = email                
                customer.save()
                return redirect ('contactinfo')
            else:
                messages.error(request, 'Emails did not match.  Could not update information.  Please try again.')
                return redirect ('contactinfo')
        else:
            data = cartData(request)
            cartItems = data['cartItems']
            order = data['order']
            items = data['items']
            customer = get_object_or_404(Customer, user=request.user)
            addresses = customer.shippingaddress_set.all()
            previous_address = {}
            for address in addresses:
                if(address):
                    previous_address['address'] = address.address
                    previous_address['city'] = address.city
                    previous_address['state'] = address.state
                    previous_address['zipcode'] = address.zipcode
                    break	       
            context = {
                'customer': customer,
                'address': previous_address,
                'cartItems': cartItems,
            }        
            return render(request, 'accounts/contactinfo.html', context)
    
    else:
        messages.error(request, 'Please login to gain access to dashboard.')
        return redirect ('login')

