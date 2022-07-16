from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  username = models.CharField(max_length=255)
  name = models.CharField(max_length=255,null=True,blank=True)
  email = models.EmailField()
  age = models.IntegerField(null=True,blank=True)
  phone_number = models.CharField(max_length=13,null=True,blank=True)
  blood_group = models.CharField(max_length=255,null=True,blank=True)
  doctor = models.CharField(max_length=255,null=True,blank=True)
  doctor_number = models.CharField(max_length=13,null=True,blank=True)
  emergency_contact = models.CharField(max_length=13,null=True,blank=True)
  profile_pic = models.FileField(upload_to="profile/",default="defaults/profile.svg",blank=True)
  
  def __str__(self):
    return self.user.username
  
  
@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
  if created:
    profile = Profile()
    profile.user = instance
    profile.username = instance.username
    profile.name = f"{instance.first_name} {instance.last_name}"
    profile.email = instance.email
    profile.save()
    instance.profile = profile
    instance.save()
  else:
    profile = Profile.objects.get(user=instance)
    profile.user = instance
    profile.username = instance.username
    profile.name = f"{instance.first_name} {instance.last_name}"
    profile.email = instance.email
    profile.save()
    
