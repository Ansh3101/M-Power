from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import Profile


def login_user(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      messages.success(request,"Logged In Successfully!")
      return redirect('edit')
    else:
      messages.error(request,"User or Password Incorrect")
      return redirect('login')
  return render(request,'users/login.html')

def signup_user(request):
  if request.method == "POST":
    try:
      username = request.POST["username"]
      email = request.POST["email"]
      password = request.POST["password"]
      user = User()
      user.username = username
      user.email = email
      user.password = password
      user.save()
      login(request,user)
      messages.success(request,"Account Created Successfully!")
      return redirect('edit')
    except :
      messages.error(request,"Error Creating Account, Try Again!")
      return redirect('signup')
  return render(request,'users/signup.html')

@login_required
def profile(request):
  return render(request,'users/profile.html')

@login_required
def logout_user(request):
  logout(request)
  return redirect('login')

@login_required
def edit_profile(request):
  if request.method == "POST":
    user = Profile.objects.get(user=request.user)
    user.username = request.POST["username"]
    user.name = request.POST["name"]
    user.email = request.POST["email"]
    if request.POST["age"] != "":
      user.age = request.POST["age"]
    user.phone_number = request.POST["phone_number"]
    if request.POST["blood_group"] != "Open this select menu":
      user.blood_group = request.POST["blood_group"]
    user.doctor = request.POST["doctor"]
    user.doctor_number = request.POST["doctor_phone_number"]
    user.emergency_contact = request.POST["emergency_contact"]
    try:
      user.profile_pic = request.FILES["profile_pic"]
    except:
      pass
    user.save()
    return redirect('profile')
  profile = Profile.objects.get(user=request.user)
  context = {
    'profile' : profile
  }
  return render(request,'users/edit.html',context)