from django.db import models
from django.contrib.auth.models import User
from store.models import Customer

class PrimaryAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    most_recent = models.BooleanField(default=False, null=True,blank=True)

    def __str__(self):
        return self.address + " " + self.city + ", " + self.state + " " + self.zipcode
