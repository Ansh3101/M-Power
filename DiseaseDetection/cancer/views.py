from time import sleep
from django.shortcuts import render,redirect
from cancer.models import LungReport,LungCancerText
from .forms import LungCancerTextForm
import pickle 
import sklearn
import pandas as pd
import os 

def convert_bool(string):
  if string == "True":
    return True
  else:
    return False

model = pickle.load(open(f'{os.path.abspath("")}/Models/finalized_model.sav', 'rb'))

def lung_cancer(request):
  form = LungCancerTextForm()
  if request.method == "POST":
    form = LungCancerTextForm(request.POST)
    gender = convert_bool(request.POST["gender"])
    age = request.POST["age"]
    smoking = convert_bool(request.POST["smoking"])
    yellow = convert_bool(request.POST["yellow_fingers"])
    anxiety = convert_bool(request.POST["anxiety"])
    peer = convert_bool(request.POST["peer_pressure"])
    chronic = convert_bool(request.POST["chronic_disease"])
    fatigue = convert_bool(request.POST["fatigue"])
    allergy = convert_bool(request.POST["allergy"])
    wheezing = convert_bool(request.POST["wheezing"])
    alcohol = convert_bool(request.POST["alcohol_consumption"])
    coughing = convert_bool(request.POST["coughing"])
    shortness_of_breadth = convert_bool(request.POST["shortness_of_breadth"])
    swallowing_difficulty = convert_bool(request.POST["swallowing_difficulty"])
    chest_pain = convert_bool(request.POST["chest_pain"])
    data = pd.DataFrame([[gender,age,smoking,yellow,anxiety,peer,chronic,fatigue,allergy,wheezing,alcohol,coughing,shortness_of_breadth,swallowing_difficulty,chest_pain]])
    result = model.predict(data)[0]
    result = "The state of your lung is very bad. Please consult a doctor."
    if form.is_valid():
      data = form.save()
      report = LungReport()
      report.data = data
      report.user = request.user.profile
      report.result = result
      report.save()
      return redirect(f'/disease/results?result={result}')
  context = {
    'form':form,
  }
  return render(request,'cancer/lung_cancer.html',context)


def brest_cancer(request):
  return render(request,'cancer/brest_cancer.html')

def result_page(request):
  result = request.GET["result"]
  context = {
    'result':result
  }
  return render(request,"cancer/result_page.html",context)

def details(request,id):
  lung_data = LungCancerText.objects.get(id=id)
  print(lung_data)
  context = {'detail':lung_data}
  return render(request,'cancer/details.html',context)