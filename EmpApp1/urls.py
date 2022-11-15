from django.urls import path
from EmpApp1.views import inicio, depto, inquilino, ganancias, formulario_depto, reserva_depto, formulario_ganancia, formulario_inquilino, registro_ganancia, registro_inquilino

urlpatterns = [
    path('', inicio,),

    path('depto/', depto, name="depto"),
    path('inquilino/', inquilino, name="inquilino"),
    path('ganancias/', ganancias, name="ganancias"),

    path('formulario_depto/',formulario_depto , name="formulario_depto"),
    path('lista_reserva/', reserva_depto , name="reserva_depto"),

    path('formulario_ganancia/',formulario_ganancia , name="formulario_ganancia"),
    path('lista_ganancia/',registro_ganancia , name="lista_ganancia"),

    path('formulario_inquilindo/',formulario_inquilino , name="formulario_inquilino"),
    path('lista_inquilino/',registro_inquilino , name="lista_inquilino"),


    
]
