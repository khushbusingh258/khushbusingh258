from django.shortcuts import render ,HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    return render(request,"home.html",{})

def login(request):
    return render(request,'login.html',{})

def blank(request):
    return render(request,'blank.html',{})
