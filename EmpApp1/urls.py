from django.urls import path
from EmpApp1.views import inicio, depto, inquilino, ganancias

urlpatterns = [
    path('', inicio,),
    path('depto/', depto, name="depto"),
    path('inquilino/', inquilino, name="inquilino"),
    path('ganancias/', ganancias, name="ganancias"),
    
]
