from django.shortcuts import render,redirect
from numpy import require
from cancer.models import BrestCancerReport, LungReport,LungCancerText
from .forms import LungCancerTextForm,BrestCancerForm
import pickle 
import pandas as pd
import os 
import joblib

def convert_bool(string):
  if string == "True":
    return True
  else:
    return False

lung_model = pickle.load(open(f'{os.path.abspath("")}/Models/finalized_model.sav', 'rb'))
brest_model = joblib.load(f'{os.path.abspath("")}/Models/brest_cancer.joblib')["model"]

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
    result = lung_model.predict(data)[0]
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


def result_page(request):
  result = request.GET["result"]
  context = {
    'result':result
  }
  return render(request,"cancer/result_page.html",context)

def brest_cancer(request):
  if request.method == "POST":
    form = BrestCancerForm(request.POST)
    if form.is_valid():
      _data = form.save(commit=False)
      form.user = request.user.profile
      form.save()
      print("Valid")
    else:
      print(form.errors)
    data = []
    for key,value in form.data.items():
      if (key == "csrfmiddlewaretoken") or (key == "method"):
        continue
      data.append(value)
    pred = brest_model.predict(data)
    if pred == 1 :
      result = "You have been diagnosed with the present cancer. We advise you to consult a doctor."
    else:
      result = "The diagnosis has not shown presence of cancer. if you still feel difficulty ,please consult a doctor."
    report = BrestCancerReport()
    report.user = request.user.profile
    report.result = result
    report.data = _data
    report.save()
    return redirect(f'/disease/results?result={result}')
  form = BrestCancerForm()
  context = {
    'form' : form
  }
  return render(request,'cancer/brest_cancer.html',context)