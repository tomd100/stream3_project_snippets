from django.conf.urls import url
from django.contrib import admin

from accounts.views import login, logout

urlpatterns = [
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
]



