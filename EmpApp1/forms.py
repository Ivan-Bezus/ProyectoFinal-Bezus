from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class Formulario_depto(forms.Form):
    
    fecha_entrada = forms.DateField() 
    fecha_salida = forms.DateField()

class Formulario_inquilino(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    dni = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60)

class Formulario_ganancia(forms.Form):
    precio_x_dia = forms.CharField(max_length=30)
    costo_gestion = forms.CharField(max_length= 30)
    costo_mant = forms.CharField(max_length=30)
    costo_limpieza = forms.CharField(max_length=30)
    ganancia = forms.CharField(max_length=30)

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


