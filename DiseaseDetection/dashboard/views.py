from django.shortcuts import render

def landing(request):
  return render(request,'index.html')

def dashboard(request):
  cancer_reports = request.user.profile.lungreport_set.all()
  eye_reports = request.user.profile.eyereport_set.all()
  heart_reports = request.user.profile.heartreport_set.all()
  context = {'cancer_reports':cancer_reports,'eye_reports':eye_reports,'heart_reports':heart_reports}
  return render(request,'dashboard/dashboard.html',context)