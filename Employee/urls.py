from django import views
from django.contrib import admin
from django.urls import path,include
from Employee import views

urlpatterns = [
    
     path('add/',views.addemployee),
     path('view/',views.viewEmployee),
     path('delete/',views.deleteEmployee),
      path('update/',views.updateEmployee),



]
