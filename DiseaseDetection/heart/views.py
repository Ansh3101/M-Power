from django.shortcuts import render
import joblib
import catboost as cb
import os 

data = joblib.load(f'{os.path.abspath("")}/Models/model.joblib')
model = data["model"]


def heartDisease(request):
  return render(request,'heart/upload.html',)