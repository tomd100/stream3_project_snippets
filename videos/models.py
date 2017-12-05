from django.db import models
from django.core.validators import *
from django.contrib import auth, messages

# Create your models here.
#-------------------------------------------------------------------------------

class VideoItem(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=500, blank=False)
    url = models.URLField(max_length=500, blank=False)
    start = models.FloatField(default = 0)
    end = models.FloatField(default = 0)
    
    def __str__(self):
        return self.title;
        
#-------------------------------------------------------------------------------

class SnippetItem(models.Model):
    video = models.ForeignKey(VideoItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False)
    start = models.FloatField(default = 0)
    end = models.FloatField(default = 0)
    
    def __str__(self):
        return self.title;
        
#-------------------------------------------------------------------------------        

