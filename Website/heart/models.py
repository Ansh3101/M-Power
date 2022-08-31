from django.db import models
from users.models import Profile

class HeartCancerText(models.Model):
  choices = ((1,'Yes'),(0,'No'))
  gender = ((1,'Male'),(0,'Female'))
  age_categories = ((0,'18-24'),(1,'25-29',),(2,'30-34',),(3,'35-39',),(4,'40-44',),(5,'45-49',),(6,'50-54',),(7,'55-59',),(8,'60-64',),(9,'65-69',),(10,'70-74',),(11,'75-79',),(12,'80 or older)'),)
  race_choices = ((0,'American Indian/Alaskan Native'),(1,'Asian',),(2,'Black',),(3,'Hispanic',),(4,'Other',),(5,'White'),)  
  diabetes_choices = ((0,'No'), (1,'No, borderline diabetes'),(2,'Yes'),(3,'Yes (during pregnancy)'))
  gen_choices = ((0,'Excellent'),(1, 'Fair'), (2,'Good'), (3,'Poor'), (4,'Very good'))
  asthma_choices = ((1,'Yes'),(0,'No'))
  kidney_choices = ((1,'Yes'),(0,'No'))
  skin_choices = ((1,'Yes'),(0,'No'))
  bmi = models.DecimalField(decimal_places=3,max_digits=5)
  smoking = models.IntegerField(choices=choices,)
  alcohol = models.IntegerField(choices=choices)  
  stroke = models.IntegerField(choices=choices)
  physical_health = models.IntegerField()
  mental_heath = models.IntegerField()
  diff_walking = models.CharField(max_length=255,choices=choices)
  gender = models.CharField(max_length=255,choices=gender)
  age_category = models.IntegerField(choices=age_categories)
  race = models.IntegerField(choices=race_choices)
  diabetic  = models.IntegerField(choices=diabetes_choices)
  gen_health = models.IntegerField(choices=gen_choices)
  sleep_time = models.DecimalField(decimal_places=3,max_digits=5)
  physical_activity = models.IntegerField(choices=asthma_choices)
  asthma = models.IntegerField(choices=asthma_choices)
  kidney_disease = models.IntegerField(choices=kidney_choices)
  skin_cancer = models.IntegerField(choices=skin_choices)
  
  def __str__(self):
    return str(self.id)
  
class HeartReport(models.Model):
  user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
  date = models.DateTimeField(auto_now_add=True)
  result = models.TextField(null=True,blank=True)
  
  def __str__(self):
    return str(self.id)