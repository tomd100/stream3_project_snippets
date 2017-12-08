from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django import forms

#-------------------------------------------------------------------------------

# # Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="avatars", blank=True, null=True)
    sub_type = models.IntegerField(blank=False, default=0)
    sub_start_date=models.DateField(blank=False, default=timezone.now)
    sub_nextreset_date=models.DateField(blank=False, default=timezone.now)

@receiver(post_save, sender=User)   # why are these in separate functions?
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
#-------------------------------------------------------------------------------

class Subscription(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

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
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)

#-------------------------------------------------------------------------------        