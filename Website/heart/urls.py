from django.urls import path
from . import views

urlpatterns = [
    path('',views.heartDisease,name="heart-disease")
]
