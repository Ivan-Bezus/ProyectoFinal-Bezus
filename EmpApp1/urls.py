from django.urls import path
from .views import inicio, inquilino, ganancias

urlpatterns = [
    path('', inicio,),
    path('inquilino/', inquilino,),
    path('ganancias/', ganancias,),
    
]
