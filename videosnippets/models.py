from django.db import models
from django.core.validators import *
from django.contrib import auth, messages
from videos.models import VideoItem

#-------------------------------------------------------------------------------

class SnippetItem(models.Model):
    video = models.ForeignKey(VideoItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False)
    start = models.FloatField(default = 0)
    end = models.FloatField(default = 0)
    jump = models.FloatField(default = 2)
    
    
    def __str__(self):
        return self.title;
        
