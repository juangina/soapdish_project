from django.shortcuts import render
from store.utils import cookieCart, cartData, guestOrder
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document

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

class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('document_upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context