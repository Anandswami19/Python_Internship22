# from xml.etree.ElementInclude import include
# from django import urls
# from django.contrib import admin
from django.urls import path,include
from group import views
urlpatterns = [
    
    path('add/',views.group),
    path('contactUS/',views.ContactUs),
    path('aboutus/',views.aboutus),
    
    path('',views.index),
    


]

