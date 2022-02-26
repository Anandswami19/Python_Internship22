from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addproduct(request):
    print("addProduct called..")
    return HttpResponse("addproduct called....")
#create view product function to display the product page
def viewproduct(request):
    return HttpResponse("view called....")

#create view product function to display the product page

def productpage(request):
    return render(request,'product/productpage.html')