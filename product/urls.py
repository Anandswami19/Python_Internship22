#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from product import views
urlpatterns = [
    path('addproduct/',views.addproduct),
    path('viewproduct/',views.viewproduct),
    path('productpage/',views.productpage),
]