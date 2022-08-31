from django.urls import path 
from . import views

urlpatterns = [
  path('lung-cancer/',views.lung_cancer,name="lung-cancer"),
  path('brest-cancer/',views.brest_cancer,name="brest-cancer"),
  path('results/',views.result_page,name="result-page"),
]
