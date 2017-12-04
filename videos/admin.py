from django.contrib import admin
from .models import VideoItem, SnippetItem

# Register your models here.
admin.site.register(VideoItem)
admin.site.register(SnippetItem)