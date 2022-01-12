from django.shortcuts import render
from store.utils import cookieCart, cartData, guestOrder
from blog.models import Posts

# Create your views here.
def posts(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    posts = Posts.objects.using('blog').order_by('-created_at')[:3]

    context = {
        'posts': posts,
        'cartItems': cartItems,
    }

    return render(request, 'blog/posts.html', context)