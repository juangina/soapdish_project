from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bars.choices import price_choices, fragrance_choices, colorants_choices
from bars.models import Bar
from blog.models import Posts
from creators.models import Creator
from .models import Video
from store.utils import cookieCart, cartData, guestOrder
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    bars = Bar.objects.order_by('-batch_code')[:3]
    barslist = Bar.objects.order_by('-batch_code')[:4]
    barslist = list(barslist)
    
    if Video.objects.filter(name='Soap Dish - Welcome').exists():
        video = Video.objects.get(name='Soap Dish - Welcome')
    else:
        video = ""

    context = {
        'bars': bars,
        'barslist': barslist,
        'price_choices': price_choices,
        'colorants_choices': colorants_choices,
        'fragrance_choices': fragrance_choices,
        'cartItems': cartItems,
        # 'video': video
    }

    return render(request, 'pages/index.html', context)

def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    creators = Creator.objects.order_by('hire_date')
    mvc_creators = Creator.objects.all().filter(is_mvc=True)
    
    if Video.objects.filter(name='Soap Dish - Welcome').exists():
        video = Video.objects.get(name='Soap Dish - Welcome')
    else:
        video = ""
    
    posts = Posts.objects.using('blog_db').order_by('-created_at')[:3]

    context = {
        'creators': creators,
        'mvc_creators': mvc_creators,
        'cartItems':cartItems,
        'video': video,
        'posts': posts
    }
    return render(request, 'pages/about.html', context)

class BarListView(ListView):
    # model = Bar
    template_name = "pages/class_view_list.html"
    context_object_name = 'bars'

    # class attribute to override the default model.object.all() queryset
    queryset = Bar.objects.order_by('-batch_code')[:3]


    def get_context_data(self, **kwargs):
        print("self.args: ", self.args)
        print("self.kwargs: ", self.kwargs)
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['creators'] = Creator.objects.all()
        return context

class CreatorBarListView(ListView):
    # model = Bar
    template_name = "pages/param_class_view_list.html"
    context_object_name = 'creator_bars'

    def get_queryset(self):
       self.creator = get_object_or_404(Creator, name=self.kwargs['creator'])
       return Bar.objects.filter(creator=self.creator)


    def get_context_data(self, **kwargs):
        print("self.args: ", self.args)
        print("self.kwargs: ", self.kwargs)
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of a single creator
        self.creator = get_object_or_404(Creator, name=self.kwargs['creator'])
        context['creator'] = self.creator
        return context

class BarDetailView(DetailView):
    model = Bar
    template_name = "pages/class_view_detail.html"
    contect_object_name = 'bar'

    
        
