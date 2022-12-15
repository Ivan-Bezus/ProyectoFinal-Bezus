from dataclasses import fields
from EmpApp1.models import Booking
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Form_person(forms.Form):

    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    dni = forms.CharField(max_length=20)
    tel = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60)

class Form_booking(forms.Form):
    
    person = forms.CharField(max_length=30)
    date_in = forms.DateField() 
    date_out = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        date_in_c = cleaned_data.get("date_in")
        date_out_c = cleaned_data.get("date_out")

        based_date = Booking.objects.all ()
        based_date_in = based_date.get("date_in")
        based_date_out = based_date.get("date_out")

    #Actualmente no estoy pudiendo ingresar a la los datos cargados en el formulario para compararlos con con los de la base de datos y saber si hay disponibilidad.
        for date in based_date: 
            if date_in_c > based_date_out and date_out_c < based_date_in:
                raise ValidationError ("No hay disponibilidad en las fechas indicadas.")
            return cleaned_data

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
        model = User
        fields = ['email','first_name', 'last_name', 'password1', 'password2']

    #Validacion de contraseñas 1 y 2 dentro del formulario, y que guarde la contraseña1.
    #El "self" tiene guardado un objeto con la informacion del formulario. La data (informacion) esta dentro del metodo "clean_date"
    def clear_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError ("Las contraseñas no coinciden")
        return password2    

# Se crea un nuevo formulario con los campos que deseo: (ModelForm)
class UsuarioRegisterForm(UserCreationForm):
    class Metal:

        model = User
        fields = ('__all__'), #instanciando de esta manera se traen todos los atributos, luego defino cualos son los atributos que deseo traer y los agrego como una lista.
        #fields = ('username', 'first_name', 'last_name', 'email')


