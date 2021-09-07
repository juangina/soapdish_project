from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Conversation_Meta(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    dialog_started = models.BooleanField(default=False,null=True, blank=True)
    dialog_completed = models.BooleanField(default=False,null=True, blank=True)
    temp_data = models.CharField(default='', max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Conversation_Dialog(models.Model):
    conversation_meta = models.ForeignKey(Conversation_Meta, on_delete=models.CASCADE)
    dialog = models.CharField(max_length=200)
    intent = models.CharField(default='None', max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.id