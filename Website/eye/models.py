from django.db import models
from users.models import Profile

class EyeReport(models.Model):
  user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
  date = models.DateTimeField(auto_now_add=True,null=True)
  scan = models.FileField(upload_to="eye",null=True,blank=True)
  result = models.TextField()
  
  def __str__(self):
    return str(self.id)