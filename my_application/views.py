from django.shortcuts import render 
from django.http import HttpResponse
from pathlib import Path
import os

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    return render(request,"home.html")
def product(request):
    username=request.POST["firstname"]
    password=request.POST["pwd"]
    return render(request,"product.html",{"firstname":username,"password":password})