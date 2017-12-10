from django.contrib import admin
from .models import Subscription, Order, OrderLineItem

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Order)
admin.site.register(OrderLineItem)