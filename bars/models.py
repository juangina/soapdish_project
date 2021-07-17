from django.db import models
from datetime import datetime
from creators.models import Creator

class Bars(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    recipe = models.CharField(default='Brambleberry', max_length=100)
    fragrance = models.CharField(default='Sans', max_length=100)
    batch_code = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    colorants = models.TextField(max_length=200, blank=True)
    nutrients = models.TextField(max_length=200, blank=True)
    exfolients = models.TextField(max_length=200, blank=True)
    price = models.IntegerField(default=5)
    discount = models.IntegerField(default=8)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)    
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_cured = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Bar(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    recipe = models.CharField(default='Brambleberry', max_length=100)
    fragrance = models.CharField(default='Sans', max_length=100)
    batch_code = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    colorants = models.TextField(max_length=200, blank=True)
    nutrients = models.TextField(max_length=200, blank=True)
    exfolients = models.TextField(max_length=200, blank=True)
    price = models.IntegerField(default=5)
    discount = models.IntegerField(default=8)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)    
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_cured = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
