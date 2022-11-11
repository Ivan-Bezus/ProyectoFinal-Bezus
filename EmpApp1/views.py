from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio (request):
   return render(request, "inicio.html") 
   
def depto (request):
    return render(request, "depto.html") 

def inquilino (request):
    return render(request, "inquilino.html") 

    
def ganancias (request):
    return render(request, "ganancias.html") 
    
   