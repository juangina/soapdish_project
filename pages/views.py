from django.shortcuts import render
from django.http import HttpResponse

from creators.models import Creator
from bars.models import Bar

def index(request):
    bars = Bar.objects.order_by('-created_date')
    context = {
        'bars': bars
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