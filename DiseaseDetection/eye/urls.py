from django.urls import path
from . import views

urlpatterns = [
    path('cataract/',views.cataract,name="cataract")
]
