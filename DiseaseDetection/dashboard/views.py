from django.shortcuts import render

def landing(request):
  return render(request,'index.html')

def dashboard(request):
  cancer_reports = request.user.profile.lungreport_set.all()
  context = {'cancer_reports':cancer_reports}
  return render(request,'dashboard/dashboard.html',context)