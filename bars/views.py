from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from bars.choices import price_choices, fragrance_choices, colorants_choices, exfolients_choices
from store.utils import cookieCart, cartData, guestOrder
from .models import Bar
from .utils import buttonPaginator

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    bars = Bar.objects.order_by('created_date').filter(for_sale=True)
    number_of_bars = bars.count()

    paginator = Paginator(bars, 12)
    page = request.GET.get('page')

    if page:
        paged_bars = paginator.get_page(page)
    else:
        page=1
        paged_bars = paginator.get_page(page)

    custom_range = buttonPaginator(3, paginator, page, paged_bars)

    context = {
            'price_choices': price_choices,
            'colorants_choices': colorants_choices,
            'fragrance_choices': fragrance_choices,
            'exfolients_choices': exfolients_choices,
            'bars': paged_bars,
            'custom_range': custom_range,
            'number_of_bars': number_of_bars,
            'values': request.GET,
            'cartItems': cartItems,
            'search': '0',
            }

    return render(request, 'bars/bars.html', context)

def bar(request, bar_id):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
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

    queryset_list = Bar.objects.order_by('created_date').filter(for_sale=True)

    
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
            queryset_list = queryset_list.filter(fragrance__icontains=fragrance)
    # Search for Colorant in colorant
    if 'colorant' in request.GET:
        colorant = request.GET['colorant']
        if colorant:
            queryset_list = queryset_list.filter(colorants__icontains=colorant)
    # Search for Exfolient in exfolient
    if 'exfolient' in request.GET:
        exfolient = request.GET['exfolient']
        if exfolient:
            queryset_list = queryset_list.filter(exfolients__icontains=exfolient)
    # Search for Price in price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    number_of_bars = queryset_list.count()

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')

    if page:
        paged_bars = paginator.get_page(page)
    else:
        page=1
        paged_bars = paginator.get_page(page)

    custom_range = buttonPaginator(4, paginator, page, paged_bars)
    #print('request.GET: ', request.GET)

    context = {
        'price_choices': price_choices,
        'colorants_choices': colorants_choices,
        'fragrance_choices': fragrance_choices,
        'exfolients_choices': exfolients_choices,
        'bars': paged_bars,
        'custom_range': custom_range,
        'number_of_bars': number_of_bars,
        'values': request.GET,
        'cartItems': cartItems,
        'search': '1',
    }
    return render(request, 'bars/bars.html', context)