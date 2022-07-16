from django.db import models

class BrestCancerText(models.Model):
  bmi = models.IntegerField()
  smoking = models.CharField(choices=)
  alcohol = models.CharField(choices=)  
  stroke = models.CharField()
  physical_health = models.DecimalField()
  mental_heath = models.CharField()
  diff_walking = models.CharField()
  gender = models.CharField()
  age_category = models.DecimalField()
  race = models.DecimalField()
  diabetic  = models.DecimalField()
  GenHealth = models.DecimalField()
  SleepTime = models.DecimalField()
  Asthma = models.DecimalField()
  kidney_disease = models.DecimalField() 
  skin_cancer = models.DecimalField()