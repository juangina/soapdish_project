from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from bars.choices import price_choices, fragrance_choices, colorants_choices
from .models import Bar
from store.utils import cookieCart, cartData, guestOrder

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    bars = Bar.objects.order_by('-created_date')

    paginator = Paginator(bars, 3)
    page = request.GET.get('page')
    paged_bars = paginator.get_page(page)

    context = {
        'bars': paged_bars,
        'cartItems': cartItems
        }
    return render(request, 'bars/bars.html', context)

def bar(request, bar_id):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    #bar = bar.objects.get(id=bar_id)
    bar = get_object_or_404(Bar, pk=bar_id)
    
    context = {
        'bar': bar,
        'cartItems': cartItems        
    }
    return render(request, 'bars/bar.html', context)

def search(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    queryset_list = Bar.objects.order_by('-created_date')

    # Search for Keywords in recipe
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # Search for Name in name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)
    # Search for Fragrance in fragrance
    if 'fragrance' in request.GET:
        fragrance = request.GET['fragrance']
        if fragrance:
            queryset_list = queryset_list.filter(fragrance__iexact=fragrance)
    # Search for Colorant in colorant
    if 'colorant' in request.GET:
        colorant = request.GET['colorant']
        if colorant:
            queryset_list = queryset_list.filter(colorants__icontains=colorant)
    # Search for Price in price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'colorants_choices': colorants_choices,
        'fragrance_choices': fragrance_choices,
        'bars': queryset_list,
        'values': request.GET,
        'cartItems': cartItems
    }
    return render(request, 'bars/search.html', context)