from django.conf.urls import url
from django.contrib import admin

from accounts.views import login, logout, register, profile

urlpatterns = [
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r"^profile$", profile, name="profile"),
]



