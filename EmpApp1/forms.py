from dataclasses import fields
from EmpApp1.models import Booking
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from EmpApp1.booking_functions.person_validation import person_f_n_valid

class Form_person(forms.Form):

    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    dni = forms.CharField(max_length=20)
    tel = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60)

    def clean_fist_name(self):
        
        f_n=self.cleaned_data.get('first_name')

        if person_f_n_valid(f_n) == False:
            return redirect ('/emp-app1/person_create_error', permanent=True)
            
        else:
            return f_n
            
    def clean_last_name(self):
        f_n=self.cleaned_data.get('first_name')
        if person_f_n_valid(f_n):
            return f_n
        else:
            return redirect ('/emp-app1/person_create_error', permanent=True)

class Form_booking(forms.Form):
    
    person = forms.CharField(max_length=30)
    date_in = forms.DateField() 
    date_out = forms.DateField()

    
class Form_gain(forms.Form):

    #reserv = forms.CharField(max_length=30)
    daily_price = forms.CharField(max_length=30)
    manag_cost = forms.CharField(max_length= 30)
    maint_cost = forms.CharField(max_length=30)
    clean_cost = forms.CharField(max_length=30)
    gain = forms.CharField(max_length=30)

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(),required= False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User #El modelo User(creado por Django-hay que importarlo) recibe los datos del usuario logeado 
        fields = ['email','first_name', 'last_name', 'password1', 'password2']

    #Validacion de contraseñas 1 y 2 dentro del formulario, y que guarde la contraseña1.
    #El "self" tiene guardado un objeto con la informacion que se llenó en el formulario. La data (informacion) esta dentro del metodo "clean_data"
    def clear_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError ("Las contraseñas no coinciden")
        return password2    #retorna lo que va a guardar en la variable correspondiente

# Se crea un nuevo formulario con los campos que deseo: (ModelForm)
class UsuarioRegisterForm(UserCreationForm):
    class Metal:

        model = User
        fields = ('__all__'), #instanciando de esta manera se traen todos los atributos, luego defino cualos son los atributos que deseo traer y los agrego como una lista.
        #fields = ('username', 'first_name', 'last_name', 'email')


