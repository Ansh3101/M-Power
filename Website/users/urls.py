from django.urls import path
from . import views

urlpatterns = [
  path('login/',views.login_user,name="login"),
  path('signup/',views.signup_user,name="signup"),
  path('profile/',views.profile,name='profile'),
  path('logout/',views.logout_user,name="logout"),
  path('edit/',views.edit_profile,name='edit')
]
