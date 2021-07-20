from django.shortcuts import render
from django.http import HttpResponse
from bars.choices import price_choices, fragrance_choices, colorants_choices

from bars.models import Bar
from creators.models import Creator

# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')

def index(request):
    bars = Bar.objects.order_by('-created_date')[:3]
    context = {
        'bars': bars,
        'price_choices': price_choices,
        'colorants_choices': colorants_choices,
        'fragrance_choices': fragrance_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    creators = Creator.objects.order_by('hire_date')
    mvc_creators = Creator.objects.all().filter(is_mvc=True)
    context = {
        'creators': creators,
        'mvc_creators': mvc_creators
    }
    return render(request, 'pages/about.html', context)