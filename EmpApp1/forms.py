from django import forms

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