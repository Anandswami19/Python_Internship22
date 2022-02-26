from contextvars import Context
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def group(request):
    return HttpResponse("group called....")

def index(request):
    context={
        'Name': 'EGift',
    }
    return render (request,"group/index.html",context)    

def ContactUs(request):
    context={
        'contact_name' : ['Anand','Deep','Khushal','Ayush','Harsh']
    }

    return render(request,"group/contactUs.html",context)

def aboutus(request):
    context={
        'IsActive':True,
        'age':20,
    }
    return render(request,"group/aboutus.html",context)

    