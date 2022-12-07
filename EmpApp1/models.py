from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person (models.Model):

    
    first_name = models.CharField(max_length=30, verbose_name= 'Nombre')
    last_name = models.CharField(max_length=30, verbose_name= 'Apellido')
    dni = models.CharField(max_length=10, verbose_name='DNI')
    tel = models.CharField(max_length=30, verbose_name= 'Telefono')
    email = models.EmailField(max_length=50, verbose_name= 'Email')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'Person'
        verbose_name = 'Inquilino'
        verbose_name_plural = 'Inquilinos'
        ordering = ['last_name']

class Booking (models.Model):

    #Relacion 1:N - One Person must register for each reservation - blank or null fields are not accepted 
    person = models.ForeignKey(Person,on_delete=models.CASCADE, blank= False, null= False, verbose_name= 'Inquilino')
    date_in = models.DateField(max_length=30, verbose_name= 'Fecha de entrada') 
    date_out = models.DateField(max_length=30, verbose_name= 'Fecha de salida')
    date_registered = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.person} del {self.date_in} al {self.date_out}'

    class Meta:
        db_table = 'Booking'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['date_registered']

class Gain (models.Model):

    booking= models.ForeignKey(Booking, on_delete= models.CASCADE)
    daily_price = models.IntegerField(verbose_name= 'Precio diario')
    manag_cost = models.IntegerField(verbose_name= 'Costo de gestion')
    maint_cost = models.IntegerField(verbose_name= 'Costo de mantenimiento')
    clean_cost = models.IntegerField(verbose_name= 'Costo de limpieza')
    gain = models.IntegerField(verbose_name= 'Ganancia')

    def __str__(self):
        return f'Reserva: {self.booking} '

    class Meta:
        db_table = 'Gain'
        verbose_name = 'Ganancia'
        verbose_name_plural = 'Ganancias'
        ordering = ['id']

class Avatar (models.Model):

    #ForeignKey: atributo del modelo models que tiene un vinculo desde un modelo hacia otro modelo -
    # " : Puedo vincular un registro del modelo Avatar con un registro del modelo que yo le diga en el atributo (en este caso USER)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank= True)