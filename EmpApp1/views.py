
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Depto, Inquilino, Ganancia
from .forms import Formulario_depto, Formulario_ganancia, Formulario_inquilino

# Create your views here.

def inicio (request):
   return render(request, "inicio.html") 
   
def depto (request):
    return render(request, "depto.html") 

def inquilino (request):
    return render(request, "inquilino.html") 

    
def ganancias (request):
    return render(request, "ganancias.html") 

#Funciones registro de reservas del depto (CRUD CREAR)

def formulario_depto (request):

    if request.method == 'POST':

        formDepto = Formulario_depto(request.POST)

        if formDepto.is_valid():
            data= formDepto.cleaned_data
            ing_depto = Depto(fecha_entrada=data['fecha_entrada'], fecha_salida =data['fecha_salida'] )
            ing_depto.save()
        
        return redirect ('/depto/')

    else:
        formDepto = Formulario_depto()
    
    return render (request, "formulario_depto.html", {"formDepto":formDepto}) 
    
def reserva_depto (request):  #CRUD LEER
    lista_reserva = Depto.objects.all()
    return render (request, "depto.html", {"reservas" : lista_reserva})

#Funciones registro de inquilino del depto (CRUD CREAR)

def formulario_inquilino (request):

    if request.method == 'POST':
   
        formInqui = Formulario_inquilino(request.POST)

        if formInqui.is_valid():
            data= formInqui.cleaned_data
            inquilino = Inquilino(nombre=data['nombre'], apellido =data['apellido'], dni =data['dni'], telefono =data['telefono'], email =data['email'] )
            inquilino.save()
        
        return redirect ('/inquilino/')

    else:
        formInqui = Formulario_inquilino()
    
    return render (request, "formulario_inquilino.html", {"formInqui":formInqui}) 

def registro_inquilino (request): #CRUD LEER

    lista_inquilino = Inquilino.objects.all()
    return render (request, "lista_inquilino.html", {"inquilinos" : lista_inquilino})

#Funciones registro de ganancias del depto (CRUD CREAR)

def formulario_ganancia (request):

    if request.method == 'POST':
        formGan = Formulario_ganancia(request.POST)

        if formGan.is_valid():
            data= formGan.cleaned_data
            ing_gan = Ganancia(precio_x_dia=request.POST['precio_x_dia'], costo_gestion=request.POST['costo_gestion'], costo_mant =request.POST['costo_mant'], costo_limpieza=request.POST['costo_limpieza'], ganancia =request.POST['ganancia'] )
            ing_gan.save()
        
        return redirect ('/ganancias/')

    else:
        formGan = Formulario_ganancia()
    
        return render (request, "formulario_ganancias.html", {"formGan":formGan}) 

def registro_ganancia (request): #CRUD LEER

    lista_ganancias = Ganancia.objects.all()
    
    return render (request, "ganancias.html", {"ganancias" : lista_ganancias})    

# Busqueda por formulario
# Primero se crea la vista para abrir el formulario
def busqueda_inquilino(request):

    return render(request, 'busqueda_inquilino.html')

#Se crea la funcion que busca en el formulario
def buscar (request):
    
    buscar_apellido = request.GET('apellido')

    inquilino = Inquilino.objects.get(apellido = buscar_apellido)
    
    return render(request,'resultado_busqueda_inquilino.html', {'nombre': inquilino, 'apellido': buscar_apellido})


# Eliminar un dato de la base de datos (CRUD Borrar)

def borrar_inquilino(request, id):

    if request.method == 'POST':

        inquilino = Inquilino.objects.get(id=id)
        inquilino.delete()

        inquilinos = Inquilino.objects.all()

        return render(request, "lista_inquilino.html", {"inquilinos":inquilinos})


# Editar un dato de la base de datos (CRUD editar)
def editar_inquilino (request,id):

    inquilino = Inquilino.objects.get(id=id)

    if request.method == 'POST':

        formInqui =  Formulario_inquilino(request.POST)      

        if formInqui.is_valid():

            data= formInqui.cleaned_data

            inquilino.nombre = data['nombre'], 
            inquilino.apellido = data['apellido'], 
            inquilino.dni = data['dni'], 
            inquilino.telefono = data['telefono'], 
            inquilino.email = data['email'] 
                            
            inquilino.save()
        
            return redirect ('/inquilino/')

    else:
        formInqui = Formulario_inquilino(initial={
            'nombre' : inquilino.nombre,
            'apellido' : inquilino.apellido, 
            'dni' : inquilino.dni, 
            'telefono' : inquilino.telefono, 
            'email' : inquilino.email    
        })
    
        return render (request, "editar_inquilino.html", {"formInqui":formInqui, "id":inquilino.id})  

    
#Crar, leer, detallar, actualizar y eliminar con VISTAS BASADAS EN CLASES (Funciones de Djaclass)

class InquilinoList(ListView):

    model = Inquilino
    template_name = 'inquilino_list.html'
    context_object_name = "inquilinos" #Contexto para el template (html)

class InquilinoDetail(DetailView):
    model = Inquilino
    template_name = 'inquilino_detail.html'
    context_object_name = "inquilinos"

class InquilinoCreate(CreateView):
    model = Inquilino
    template_name = 'inquilino_create.html'
    fields = ["nombre", "apellido", "dni", "telefono", "email"]
    success_url = '/inquilino-lista/'

class InquilinoUpdate(UpdateView):
    model = Inquilino
    template_name = 'inquilino_update.html'
    fields = ['__all__']
    success_url = '/inquilino-lista/'

class InquilinoDelete(DeleteView):
    model = Inquilino
    template_name = 'inquilino_delete.html'
    success_url = '/inquilino-lista/'

