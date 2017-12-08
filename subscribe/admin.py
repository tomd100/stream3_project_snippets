from django.contrib import admin
from .models import SubscriptionType, Order, SubscriptionOrdered

# Register your models here.
admin.site.register(SubscriptionType)
admin.site.register(Order)
admin.site.register(SubscriptionOrdered)