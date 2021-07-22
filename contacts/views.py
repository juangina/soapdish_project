from django.shortcuts import render, redirect
from contacts.models import Contact
from django.contrib import messages
# from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        bar_id = request.POST['bar_id']
        bar = request.POST['bar']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        return redirect('/bars/'+bar_id)
    return
