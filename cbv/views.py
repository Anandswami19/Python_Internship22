from multiprocessing import context
from re import template
from sys import modules
from django.shortcuts import render
from django.views.generic import ListView
from .models import Hr



class Hrlist(ListView):
    model = Hr
    Hrlist= model.objects.all()
    template_name = 'cbv/Hr_list.html'
    context_object_name = 'Hrlist'



