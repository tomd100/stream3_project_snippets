from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

#-------------------------------------------------------------------------------

# Create your models here.
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