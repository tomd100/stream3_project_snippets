from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone
# from django import forms

#-------------------------------------------------------------------------------        

class Subscription(models.Model):
    type = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.description

#-------------------------------------------------------------------------------        
        
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

#-------------------------------------------------------------------------------        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    subscription = models.ForeignKey(Subscription, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.subscription.name, self.subscription.price)
        
#-------------------------------------------------------------------------------        
