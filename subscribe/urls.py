from django.conf.urls import url
from django.contrib import admin

from .views import checkout

urlpatterns = [
    url(r'^', checkout, name='checkout'),
]



