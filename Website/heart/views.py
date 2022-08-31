from django.shortcuts import render,redirect
import joblib
import catboost as cb
import os 
from .models import HeartReport
from .forms import HeartCancerForm

data = joblib.load(f'{os.path.abspath("")}/Models/heart.joblib')
model = data["model"]


def heartDisease(request):
  form = HeartCancerForm()
  if request.method == "POST":
    form = HeartCancerForm(request.POST)
    if form.is_valid():
      form.save()
    bmi = float(request.POST["bmi"])
    smoking = int(request.POST["smoking"])
    alcohol = int(request.POST["alcohol"])
    stroke = int(request.POST["stroke"])
    mental_heath = int(request.POST["mental_heath"])
    physical_health = int(request.POST["physical_health"])
    diff_walking = int(request.POST["diff_walking"])
    gender = int(request.POST["gender"])
    age_category = int(request.POST["age_category"])
    race = int(request.POST["race"])
    diabetic = int(request.POST["diabetic"])
    gen_health = int(request.POST["gen_health"])
    sleep_time = int(request.POST["sleep_time"])
    asthma = int(request.POST["asthma"])
    kidney_disease = int(request.POST["kidney_disease"])
    skin_cancer = int(request.POST["skin_cancer"])
    physical_activity = int(request.POST['physical_activity'])
    data = [bmi,smoking,alcohol,stroke,physical_health,mental_heath,diff_walking,gender,age_category,race,diabetic,physical_activity,gen_health,sleep_time,asthma,kidney_disease,skin_cancer]
    pred = model.predict(data)
    if pred == 0:
      result = "The Heart has Disease"
    else:
      result = "Your Heart is absolutely Fine"
    report = HeartReport()
    report.user = request.user.profile
    report.result = result
    report.save()
    return redirect(f'/disease/results?result={result}')
  else:
    context = {'form':form}
    return render(request,'heart/upload.html',context)