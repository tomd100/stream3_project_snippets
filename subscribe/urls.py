from django.conf.urls import url
# from django.contrib import admin

from .views import subscribe, add_to_cart, checkout


urlpatterns = [
    url(r'^$', subscribe, name='subscribe'),
    url(r'^add', add_to_cart, name='add_to_cart'),
    url(r'^checkout$', checkout, name='checkout'),
]



