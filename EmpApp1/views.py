
from urllib import request
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render


from .models import Avatar, Booking, Person, Gain
from .forms import Form_booking, Form_person, Form_gain, UserEditForm, UsuarioRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

from EmpApp1.booking_functions.availability import check_availability
from django import forms
from django.core.exceptions import ValidationError


# Create your views here.

def inicio (request):
    try:
        avatar = Avatar.objects.get(user = request.user)
        return render(request, "inicio.html", {"url": avatar.imagen.url}) 

    except:
        return render(request, "inicio.html",)

def about_me(request):
    return render(request, "about_me.html",)

def contact_me(request):
    return render(request, "contact_me.html",)

#--------------------------------------------------------------------------------------------------------
# 1 PERSON SECTION
#--------------------------------------------------------------------------------------------------------
@login_required
def person_main (request):
    return render(request, "person_main.html") 

# 1.1 CRUD: CREATE person
#--------------------------------------------------------------
class person_create (LoginRequiredMixin,CreateView):

    model = Person
    template_name = 'person_create.html'
    fields = ["first_name", "last_name", "dni", "tel", "email"]
    success_url = '/emp-app1/person-main/'

#1.2 CRUD: READ person
#-------------------------------------------------------------
class person_read (LoginRequiredMixin,ListView): 
    
    model = Person
    template_name = 'person_read.html'
    context_object_name = 'person' #Contexto para el template (html)

# 1.3 CRUD: DETAIL person
#-------------------------------------------------------------
class person_detail (DetailView):

    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'

# 1.4 CRUD: UPDATE person
#-------------------------------------------------------------
class person_update(UpdateView):

    model = Person
    template_name = 'person_update.html'
    fields = ["first_name", "last_name", "dni", "tel", "email"]
    success_url = '/emp-app1/person-read/'
    context_object_name = 'person'

# 1.5 CRUD: DELETE person
#-------------------------------------------------------------
class person_delete(DeleteView):

    model = Person
    template_name = 'person_delete.html'
    success_url = '/emp-app1/person-read/'

#--------------------------------------------------------------------------------------------------------
# 2 BOOKING SECTION
#--------------------------------------------------------------------------------------------------------
@login_required
def booking_main (request):
    return render(request, "booking_main.html")  

# 2.1 CRUD: CREATE booking
#-------------------------------------------------------------
class booking_create (LoginRequiredMixin,CreateView):

    model = Booking
    template_name = 'booking_create.html'
    fields = ["person", "date_in", "date_out"]
    success_url = '/emp-app1/booking-read/'

    def form_valid(self,form):
        cleaned_data = form.cleaned_data
        date_in_c = cleaned_data["date_in"]
        date_out_c = cleaned_data["date_out"]

        #Actualmente no estoy pudiendo ingresar a la los datos cargados en el formulario para compararlos con con los de la base de datos y saber si hay disponibilidad.
        if check_availability(date_in_c , date_out_c):
            booking = Booking.objects.create(
                person = cleaned_data['person'],
                date_in = date_in_c,   
                date_out = date_out_c,
                date_registered = cleaned_data['date_registered'],
            )
            booking.save()
            
            return HttpResponse ("Registro realizado con exito.")
        else:
            raise ValidationError ("No hay disponibilidad en las fechas indicadas.Vuelva atrás e intente nuevamente")
           

# 2.2 CRUD: READ booking
#-------------------------------------------------------------
class booking_read (LoginRequiredMixin,ListView): 
    
    model = Booking
    template_name = 'booking_read.html'
    context_object_name = "booking" #Contexto para el template (html)

# 2.3 CRUD: DETAIL booking
#-------------------------------------------------------------
class booking_detail (DetailView):

    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = "booking"

# 2.4 CRUD: UPDATE booking
#-------------------------------------------------------------
class booking_update(UpdateView):

    model = Booking
    template_name = 'booking_update.html'
    fields = ["person", "date_in", "date_out"]
    success_url = '/emp-app1/booking-read/'
    context_object_name = 'booking'

# 2.5 CRUD: DELETE booking
#-------------------------------------------------------------
class booking_delete(DeleteView):

    model = Booking
    template_name = 'booking_delete.html'
    success_url = '/emp-app1/booking-read/'

#--------------------------------------------------------------------------------------------------------
# 3 GAIN SECTION
#--------------------------------------------------------------------------------------------------------
@staff_member_required(login_url= '/emp-app1/user-login') 
def gain_main (request):
    return render(request, "gain_main.html") 

# 3.1 CRUD: CREATE gain
#-------------------------------------------------------------
class gain_create (LoginRequiredMixin,CreateView):

    model = Gain
    template_name = 'gain_create.html'
    fields = ['booking','daily_price', 'manag_cost', 'maint_cost', 'clean_cost', 'gain']
    success_url = '/emp-app1/gain-read/'

    
# 3.2 CRUD: READ gain
#-------------------------------------------------------------
class gain_read (LoginRequiredMixin,ListView): 
    
    model = Gain
    template_name = 'gain_read.html'
    context_object_name = "gain" #Contexto para el template (html)

# 3.3 CRUD: DETAIL gain
#-------------------------------------------------------------
class gain_detail (DetailView):

    model = Gain
    template_name = 'gain_detail.html'
    context_object_name = "gain"

# 3.4 CRUD: UPDATE gain
#-------------------------------------------------------------
class gain_update(UpdateView):

    model = Gain
    template_name = 'gain_update.html'
    fields = ['booking','daily_price', 'manag_cost', 'maint_cost', 'clean_cost', 'gain']
    success_url = '/emp-app1/gain-read/'
    context_object_name = 'gain'

 #2.5 CRUD: DELETE booking
#-------------------------------------------------------------
class gain_delete(DeleteView):
    model = Gain
    template_name = 'gain_delete.html'
    success_url = '/emp-app1/gain-read/'

#--------------------------------------------------------------------------------------------------------------
#LOGIN on the page
#--------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
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
        
        
        return render (request, "user_edit.html", {"mensaje" : "Las contraseñas no coinciden"})  

    else:
        #Hay problemas en esta instancia request.user REVISAR) Info en Clase 24 min 1:00:00 aprox  
        Miform = UserEditForm (instance = request.user)
        
        
        return render (request, "user_edit.html", {"Miform" : Miform})  