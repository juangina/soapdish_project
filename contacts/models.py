from django.db import models
from datetime import datetime
import uuid
from store.models import Customer

class Contact(models.Model):
    bar = models.CharField(max_length=200)
    bar_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    body = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    contact_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    recipient1 = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    recipient2 = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)        
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']