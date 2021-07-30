from django.shortcuts import render
from bars.choices import price_choices, fragrance_choices, colorants_choices
from bars.models import Bar
from creators.models import Creator
from .models import Video
from store.utils import cookieCart, cartData, guestOrder

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    bars = Bar.objects.order_by('-batch_code')[:3]
    if Video.objects.filter(name='Test Video').exists():
        video = Video.objects.get(name='Test Video')
    else:
        video = ""
    context = {
        'bars': bars,
        'price_choices': price_choices,
        'colorants_choices': colorants_choices,
        'fragrance_choices': fragrance_choices,
        'cartItems': cartItems,
        'video': video
    }

    return render(request, 'pages/index.html', context)

def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    creators = Creator.objects.order_by('hire_date')
    mvc_creators = Creator.objects.all().filter(is_mvc=True)
    context = {
        'creators': creators,
        'mvc_creators': mvc_creators,
        'cartItems':cartItems
    }
    return render(request, 'pages/about.html', context)