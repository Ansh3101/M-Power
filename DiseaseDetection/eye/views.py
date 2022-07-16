from django.shortcuts import redirect, render
from .ml import getModel,val_transforms
from .models import EyeReport
import numpy as np
import torch 
import cv2
import os
import requests
import json

ENDPOINT = 'https://eye-artificiali.herokuapp.com/eyedisease'

pred2label = {0: 'Cataracts', 1: 'Glaucoma', 2: 'Healthy', 3: 'Uveitis'}
model = getModel()

# def getPrediction(path):
#   path = f'{os.path.abspath("")}/Media/{path}'
#   image = cv2.imread(path)
#   image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#   image = val_transforms(image)
#   image = image.to('mps')
#   image = torch.reshape(image,(1,3,224,224))
#   pred = model(image).detach()
#   pred = pred.cpu()
#   pred = np.argmax(pred).item()
#   pred = pred2label[pred]
#   return pred

def cataract(request):
  if request.method == "POST":
    image = request.FILES['scan']
    data = EyeReport()
    data.scan = image
    data.user = request.user.profile
    data.save()
    # result = getPrediction(data.scan)
    path = f'{os.path.abspath("")}/Media/{data.scan}'
    files = {'file': open(path, 'rb')}
    response = requests.post(ENDPOINT, files=files)
    result = json.loads(response.text)
    result = result["Prediction"]
    data.result = result
    data.save()
    return redirect(f'/disease/results?result={result}')
  else:
    return render(request,'eye/cataract.html')
