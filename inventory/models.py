from django.db import models
from django.contrib.auth.models import User
from bars.models import Bar

def get_deleted_bar():
	return Bar.objects.get_or_create(name='delected')[0]

class Expenses(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    unit = models.CharField(max_length=200, blank=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    manufacturer = models.CharField(max_length=200, blank=True)
    distributer = models.CharField(max_length=200, blank=True)
    model_number = models.CharField(max_length=200, blank=True)
    serial_number = models.CharField(max_length=200, blank=True)
    purchase_date = models.DateTimeField(null=True, blank=True)
    purchaser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    name = models.ForeignKey(Expenses, on_delete=models.SET_NULL, null=True, blank=True)
    bar_soap = models.ForeignKey(Bar, default=None, on_delete=models.SET(get_deleted_bar), null=True, blank=True)
    quantity_available = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image = models.ImageField(null=True, blank=True)    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name.name