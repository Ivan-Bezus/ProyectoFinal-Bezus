from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio (request):
   return HttpResponse (f'Página de inicio')


def inquilino (request):
    return HttpResponse (f'Página de inquilino')
    

def ganancias (request):
    return HttpResponse (f'Página de ganancias')
   