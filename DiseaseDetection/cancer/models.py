from django.db import models
from users.models import Profile

class LungCancerText(models.Model):
  CHOICES = (('True','Yes'),('False','No'))
  GENDER_CHOICES = (('True','Male'),('False','Female'))
  user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
  gender = models.CharField(max_length=255,choices=GENDER_CHOICES)
  age  = models.IntegerField()
  smoking  = models.CharField(max_length=255,choices=CHOICES)
  yellow_fingers  = models.CharField(max_length=255,choices=CHOICES)
  anxiety  = models.CharField(max_length=255,choices=CHOICES)
  peer_pressure  = models.CharField(max_length=255,choices=CHOICES)
  chronic_disease  = models.CharField(max_length=255,choices=CHOICES)
  fatigue  = models.CharField(max_length=255,choices=CHOICES)
  allergy  = models.CharField(max_length=255,choices=CHOICES)
  wheezing  = models.CharField(max_length=255,choices=CHOICES)
  alcohol_consumption = models.CharField(max_length=255,choices=CHOICES)
  coughing  = models.CharField(max_length=255,choices=CHOICES)
  shortness_of_breadth = models.CharField(max_length=255,choices=CHOICES)
  swallowing_difficulty  = models.CharField(max_length=255,choices=CHOICES)
  chest_pain  = models.CharField(max_length=255,choices=CHOICES)
  
  def __str__(self):
    return str(self.id)
class LungReport(models.Model):
  user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
  date = models.DateTimeField(auto_now_add=True)
  result = models.TextField(null=True,blank=True)
  data = models.OneToOneField(LungCancerText,on_delete=models.CASCADE)
  
  def __str__(self):
    return str(self.id)
  