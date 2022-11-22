from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def index(request):
    #return HttpResponse("This is Django Project.")
    n=random.randint(1111,9999)
    return render(request,'index.html',{'name':n})