from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Avatar, Booking, Person, Gain
from .forms import Form_booking, Form_person, Form_gain, UserEditForm, UsuarioRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio (request):
    try:
        avatar = Avatar.objects.get(user = request.user)
        return render(request, "inicio.html", {"url": avatar.imagen.url}) 

    except:
        return render(request, "inicio.html", )

@login_required
def inquilino (request):
    return render(request, "inquilino.html") 

@staff_member_required(login_url= '/emp-app1/user-login') 
def ganancias (request):
    return render(request, "ganancias.html") 
#-------------------
# 2 BOOKING SECTION
#-------------------
def booking_main (request):
    return render(request, "booking_main.html")  

# 2.1 CRUD: Create booking
#-------------------------
def booking_create (request):

    if request.method == 'POST':

        myform = Form_booking(request.POST)

        if myform.is_valid():
            data= myform.cleaned_data
            book = Booking(person=data['person'], date_in=data['date_in'], date_out=data['date_out'] )
            book.save()
        
        return render (request, "booking_ok.html", {"myform": myform}) 

    else:
        myform = Form_booking()
    
    return render (request, "booking_create.html", {"myform": myform}) 

# #2.2 READ booking
def booking_read (request): 
    
    booking_list = Booking.objects.all()

    return render (request, "booking_read.html", {"booking":booking_list})

#Funciones registro de inquilino del depto (CRUD CREAR)

# def formulario_inquilino (request):

#     if request.method == 'POST':
   
#         formInqui = Formulario_inquilino(request.POST)

#         if formInqui.is_valid():
#             data= formInqui.cleaned_data
#             inquilino = Inquilino(nombre=data['nombre'], apellido =data['apellido'], dni =data['dni'], telefono =data['telefono'], email =data['email'] )
#             inquilino.save()
        
#         return redirect ('/inquilino/')

#     else:
#         formInqui = Formulario_inquilino()
    
#     return render (request, "formulario_inquilino.html", {"formInqui":formInqui}) 

# def registro_inquilino (request): #CRUD LEER

#     lista_inquilino = Inquilino.objects.all()
#     return render (request, "lista_inquilino.html", {"inquilinos" : lista_inquilino})

# #Funciones registro de ganancias del depto (CRUD CREAR)

# def formulario_ganancia (request):

#     if request.method == 'POST':
#         formGan = Formulario_ganancia(request.POST)

#         if formGan.is_valid():
#             data= formGan.cleaned_data
#             ing_gan = Ganancia(precio_x_dia=request.POST['precio_x_dia'], costo_gestion=request.POST['costo_gestion'], costo_mant =request.POST['costo_mant'], costo_limpieza=request.POST['costo_limpieza'], ganancia =request.POST['ganancia'] )
#             ing_gan.save()
        
#         return redirect ('/ganancias/')

#     else:
#         formGan = Formulario_ganancia()
    
#         return render (request, "formulario_ganancias.html", {"formGan":formGan}) 

# def registro_ganancia (request): #CRUD LEER

#     lista_ganancias = Ganancia.objects.all()
    
#     return render (request, "ganancias.html", {"ganancias" : lista_ganancias})    

# Busqueda por formulario
# Primero se crea la vista para abrir el formulario
# def busqueda_inquilino(request):

#     return render(request, 'busqueda_inquilino.html')

# #Se crea la funcion que busca en el formulario
# def buscar (request):
    
#     buscar_apellido = request.GET('apellido')

#     inquilino = Inquilino.objects.get(apellido = buscar_apellido)
    
#     return render(request,'resultado_busqueda_inquilino.html', {'nombre': inquilino, 'apellido': buscar_apellido})


# # Eliminar un dato de la base de datos (CRUD Borrar)

# def borrar_inquilino(request, id):

#     if request.method == 'POST':

#         inquilino = Inquilino.objects.get(id=id)
#         inquilino.delete()

#         inquilinos = Inquilino.objects.all()

#         return render(request, "lista_inquilino.html", {"inquilinos":inquilinos})
#     #Revisar: Devuelve none porque no entra en el if 


# # Editar un dato de la base de datos (CRUD editar)
# def editar_inquilino (request,id):

#     inquilino = Inquilino.objects.get(id=id)

#     if request.method == 'POST':

#         formInqui = Formulario_inquilino(request.POST)      

#         if formInqui.is_valid():

#             data= formInqui.cleaned_data
#             #Potencial problema "inquilino" ---revisar
#             inquilino.nombre = data['nombre'], 
#             inquilino.apellido = data['apellido'], 
#             inquilino.dni = data['dni'], 
#             inquilino.telefono = data['telefono'], 
#             inquilino.email = data['email'] 
                            
#             inquilino.save()
        
#             return redirect ('/inquilino/')
#         #Revisar: Devuelve "none" porque no entra en el if (VER SOLUCION EN FUNCION USER_EDIT: Agregar return cuando no entra en el IF)

#     else:
#         formInqui = Formulario_inquilino(initial={
#             'nombre' : inquilino.nombre,
#             'apellido' : inquilino.apellido, 
#             'dni' : inquilino.dni, 
#             'telefono' : inquilino.telefono, 
#             'email' : inquilino.email    
#         })
       
#         return render (request, "editar_inquilino.html", {"formInqui":formInqui, "id":inquilino.id})  
#         #(VER SOLUCION EN FUNCION USER_EDIT: Agregar return cuando no entra en el IF) ADEMAS FIJARSE EL inquilino.id
    
# #CRUD INQUILINO: Crar, leer, detallar, actualizar y eliminar con VISTAS BASADAS EN CLASES (Funciones de Djaclass)
# # Se agrega un "MIXIN" para dotar de funciones a las clases, en el caso de inquilino: Autenticacion de usuario"
# class InquilinoList(LoginRequiredMixin,ListView):

#     model = Inquilino
#     template_name = 'inquilino_list.html'
#     context_object_name = "inquilinos" #Contexto para el template (html)

# class InquilinoDetail(DetailView):
#     model = Inquilino
#     template_name = 'inquilino_detail.html'
#     context_object_name = "inquilinos"

# class InquilinoCreate(CreateView):
#     model = Inquilino
#     template_name = 'inquilino_create.html'
#     fields = ["nombre", "apellido", "dni", "telefono", "email"]
#     success_url = '/inquilino-lista/'

# class InquilinoUpdate(UpdateView):
#     model = Inquilino
#     template_name = 'inquilino_update.html'
#     fields = ['__all__']
#     success_url = '/inquilino-lista/'

# class InquilinoDelete(DeleteView):
#     model = Inquilino
#     template_name = 'inquilino_delete.html'
#     success_url = '/inquilino-lista/'


#LOGIN on the page

def user_login(request):
    
    if request.method == 'POST':
   
        Miform = AuthenticationForm(request, data = request.POST)

        if Miform.is_valid():
            data= Miform.cleaned_data

            usr = data ["username"]
            psw = data ["password"]

            user = authenticate(username = usr , password = psw) #Validacion de usuario, si no matchea alguno devuelve NONE.

            if user: 
                login(request, user)
                return render (request, "inicio.html", {"mensaje": f'Bienvenido {user} a la plataforma de la gestión de alquiler transitorio'})
            
            else: 
                return render (request, "inicio.html", {"mensaje": f'Error, datos incorrectos'})
        
        return render (request, "inicio.html", {"mensaje": f'Error, formulario invalido'})            
        
        
    else:
        Miform = AuthenticationForm()
    
    return render (request, "user_login.html", {"Miform": Miform})

#Register a new user

def user_register(request):
    if request.method == 'POST':

        #Miform = UserCreationForm(request.POST) Se puede hacer así o crear un nuevo formulario que herede sus atributos y seleccionar la informacion que quiero mostrar
        # Ver como sigue
        Miform = UsuarioRegisterForm(request.POST)

        if Miform.is_valid():
            data= Miform.cleaned_data
            usr = Miform.cleaned_data["username"]

            Miform.save()
        
            return render (request, "inicio.html", {"mensaje": f'Usuario {usr} creado con éxito.'}) 
        
        else:
            return render (request, "inicio.html", {"mensaje": f'Error al crear el usuario.'}) 

    else:
        Miform = UsuarioRegisterForm()
    
    return render (request, "user_register.html", {"Miform":Miform}) 

#Edition of registred users: create a new form "UsedEditForm" in "forms.py" with an associated model

def user_edit(request):

    usr = request.user

    if request.method == 'POST':

        Miform =  UserEditForm(request.POST)      

        if Miform.is_valid():

            data= Miform.cleaned_data

            usr.first_name = data['first_name'], 
            usr.last_name = data['last_name'], 
            usr.email = data['email'], 
            usr.set_password(data['password1']) #Para modificar la contraseña   
                                  
            usr.save()
        
            return render (request, "inicio.html", {"mensaje":'Datos actualizados con éxito.'}) 
        
        #Revisar Devuelve none porque no entra en el if "Miform = User..." (solucionado)
        return render (request, "user_edit.html", {"mensaje" : "Las contraseñas no coinciden"})  

    else:
        #Hay problemas en esta instancia request.user REVISAR) Info en Clase 24 min 1:00:00 aprox  
        Miform = UserEditForm (instance = request.user)
        
        
        return render (request, "user_edit.html", {"Miform" : Miform})  