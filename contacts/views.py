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

        # creator_email = request.POST['creator_email']

        # Check if logged in user has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(bar_id=bar_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/bars/'+bar_id)

        contact = Contact(bar_id=bar_id, bar=bar, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Send Mail
        # send_mail(
        #     'Property bar Inquiry',
        #     'There has been an inquiry for ' + bar + '. Sign into the admin panel for more information.',
        #     'jejlifestyle@theaccidentallifestyle.net',
        #     [realtor_email, 'ericrenee21@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted.  An associate will get back to you soon.')

        return redirect('/bars/'+bar_id)
    return
