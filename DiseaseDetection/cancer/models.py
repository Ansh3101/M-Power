from statistics import mode
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

class LungCancerImage(models.Model):
  scan = models.FileField(upload_to="lung-cancer/")
  def __str__(self):
    return str(self.id)
  
class LungReport(models.Model):
  user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
  date = models.DateTimeField(auto_now_add=True)
  result = models.TextField(null=True,blank=True)
  data = models.OneToOneField(LungCancerText,on_delete=models.CASCADE,null=True)
  image_data = models.OneToOneField(LungCancerImage,on_delete=models.CASCADE,null=True)
  
  def __str__(self):
    return str(self.id)

class BrestCancerText(models.Model):
  area_mean = models.DecimalField(decimal_places=255,max_digits=500)
  area_se = models.DecimalField(decimal_places=255,max_digits=500)
  area_worst = models.DecimalField(decimal_places=255,max_digits=500)
  compactness_mean = models.DecimalField(decimal_places=255,max_digits=500)
  compactness_se = models.DecimalField(decimal_places=255,max_digits=500)
  compactness_worst = models.DecimalField(decimal_places=255,max_digits=500)
  concave_points_mean = models.DecimalField(decimal_places=255,max_digits=500)
  concave_points_se = models.DecimalField(decimal_places=255,max_digits=500)
  concave_points_worst = models.DecimalField(decimal_places=255,max_digits=500)
  concavity_mean = models.DecimalField(decimal_places=255,max_digits=500)
  concavity_se = models.DecimalField(decimal_places=255,max_digits=500)
  concavity_worst = models.DecimalField(decimal_places=255,max_digits=500)
  fractal_dimension_mean = models.DecimalField(decimal_places=255,max_digits=500)
  fractal_dimension_se = models.DecimalField(decimal_places=255,max_digits=500)
  fractal_dimension_worst = models.DecimalField(decimal_places=255,max_digits=500)
  perimeter_mean = models.DecimalField(decimal_places=255,max_digits=500)
  perimeter_se = models.DecimalField(decimal_places=255,max_digits=500)
  perimeter_worst = models.DecimalField(decimal_places=255,max_digits=500)
  radius_mean = models.DecimalField(decimal_places=255,max_digits=500)
  radius_se = models.DecimalField(decimal_places=255,max_digits=500)
  radius_worst = models.DecimalField(decimal_places=255,max_digits=500)
  smoothness_mean = models.DecimalField(decimal_places=255,max_digits=500)
  smoothness_se = models.DecimalField(decimal_places=255,max_digits=500)
  smoothness_worst = models.DecimalField(decimal_places=255,max_digits=500)
  symmetry_mean = models.DecimalField(decimal_places=255,max_digits=500)
  symmetry_se = models.DecimalField(decimal_places=255,max_digits=500)
  symmetry_worst = models.DecimalField(decimal_places=255,max_digits=500)
  texture_mean = models.DecimalField(decimal_places=255,max_digits=500)
  texture_se = models.DecimalField(decimal_places=255,max_digits=500)
  texture_worst = models.DecimalField(decimal_places=255,max_digits=500)
  
  def __str__(self):
    return str(self.user)
  
class BrestCancerReport(models.Model):
  user = models.ForeignKey(Profile,on_delete=models.CASCADE)
  data = models.OneToOneField(BrestCancerText,on_delete=models.SET_NULL,null=True)
  result = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.id)