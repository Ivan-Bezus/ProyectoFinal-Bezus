from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Depto, Inquilino, Ganancia

# Create your views here.

def inicio (request):
   return render(request, "inicio.html") 
   
def depto (request):
    return render(request, "depto.html") 

def inquilino (request):
    return render(request, "inquilino.html") 

    
def ganancias (request):
    return render(request, "ganancias.html") 

#Funciones registro de reservas del depto 

def formulario_depto (request):

    if request.method == 'POST':
        ing_depto = Depto(cobro_x_día=request.POST['cobro_x_día'], fecha_entrada=request.POST['fecha_entrada'], fecha_salida =request.POST['fecha_salida'] )
        ing_depto.save()
        
        return redirect ('depto')
    else:

        return render (request, "formulario_depto.html") 
    
def reserva_depto (request): 
    lista_reserva = Depto.objects.all()
    return render (request, "depto.html", {"reservas" : lista_reserva})

#Funciones registro de inquilino del depto

def formulario_inquilino (request):

    if request.method == 'POST':
        ing_inquilino = Inquilino(nombre=request.POST['nombre'], apellido=request.POST['apellido'], dni =request.POST['dni'], telefono =request.POST['telefono'], email =request.POST['email'] )
        ing_inquilino.save()
        
        return redirect ('inquilino')
    else:

        return render (request, "formulario_inquilino.html") 

def registro_inquilino (request): 
    lista_inquilino = Inquilino.objects.all()
    return render (request, "inquilino.html", {"inquilinos" : lista_inquilino})

#Funciones registro de ganancias del depto

def formulario_ganancia (request):

    if request.method == 'POST':
        ing_ganancia = Ganancia(precio_x_dia=request.POST['precia_x_dia'], costo_gestion=request.POST['costo_gestion'], costo_mant =request.POST['costo_mant'], costo_limpieza=request.POST['costo_limpieza'], ganancia =request.POST['ganancia'] )
        ing_ganancia.save()
        
        return redirect ('inquilino')
    else:

        return render (request, "formulario_ganancias.html") 

def registro_ganancia (request): 
    lista_ganancias = Ganancia.objects.all()
    return render (request, "ganancias.html", {"ganancia" : lista_ganancias})    