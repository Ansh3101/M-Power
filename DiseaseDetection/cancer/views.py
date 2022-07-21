from django.shortcuts import render,redirect
from tensorflow import keras
import tensorflow as tf
from cancer.models import BrestCancerReport, LungReport,LungCancerImage
from keras.preprocessing.image import load_img
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.applications.vgg16 import preprocess_input
from .forms import LungCancerTextForm,BrestCancerForm
import numpy as np
import pickle 
import random
import pandas as pd
import os 
import joblib
import cv2 


classes = {0:'You have been diagnosed with Adenocarcinoma in the lungs. It may be cured if the entire tumor is removed surgically or destroyed with radiation.We urge you to consult medical attention immediately.',1: 'Large Cell Carcinoma',2:"You don't have the presence of cancer in you lungs. If problems still arise then you may consider consulting a doctor.",3:'Squamous Cell Carcinoma'}

def convert_bool(string):
  if string == "True":
    return True
  else:
    return False

lung_model = pickle.load(open(f'{os.path.abspath("")}/Models/finalized_model.sav', 'rb'))
brest_model = joblib.load(f'{os.path.abspath("")}/Models/brest_cancer.joblib')["model"]
lung_image_model = keras.models.load_model("/Users/deveshkedia/Desktop/Projects/Doing/M-Power/DiseaseDetection/Models/lung-image.hdf5")

def lung_cancer(request):
  form = LungCancerTextForm()
  if request.method == "POST":
    if request.POST["method"] == "text":
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
      print(result)
      if result == 0:
        result = "You don't have the presence of cancer in you lungs. If problems still arise then you may consider consulting a doctor."
      else:
        result = "You have been diagnosed with lung cancer. We recommend you to consult a doctor urgently or even consider getting hospitalized."
      if form.is_valid():
        data = form.save()
        report = LungReport()
        report.data = data
        report.user = request.user.profile
        report.result = result
        report.save()
        return redirect(f'/disease/results?result={result}')
    else:
      image = request.FILES["scan"]
      data = LungCancerImage()
      data.scan = image
      data.save()
      img = load_img(data.scan.path, target_size=(350, 350))
      img = img_to_array(img)
      img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
      img = preprocess_input(img)
      print(img.shape)
      pred = lung_image_model.predict(img)
      pred = np.argmax(pred)
      pred = classes[pred]
      report = LungReport.objects.create(user=request.user.profile,result=pred,image_data=data)
      data.save()
      return redirect(f'/disease/results?result={pred}')
      
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