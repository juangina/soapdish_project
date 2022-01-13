from django.shortcuts import render
from store.utils import cookieCart, cartData, guestOrder
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def dashboard(request): 
    if request.user.is_authenticated and request.user.is_staff:
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']


        context = {
            'cartItems': cartItems,
        }

        return render(request, 'dev_app/dashboard.html', context)
    else:
        return(request, 'dev_app/no_access_allowed.html')
