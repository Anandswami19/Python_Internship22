from django.contrib import admin
from venv import create
from django.urls import include,path
from .views import CreateTask,DeleteTask,UpdateTask,TaskDetail
from Task import views

urlpatterns = [
   
     path('add/', CreateTask.as_view()),
     #path('view/',views.index),
     path('<pk>/delete/', DeleteTask.as_view()),
     path('<pk>/Update/', UpdateTask.as_view()),
     path('<pk>/view/', TaskDetail.as_view()),



]