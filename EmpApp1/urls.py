from django.urls import path

from EmpApp1.views import(
InquilinoList,
InquilinoDetail,
InquilinoCreate, 
InquilinoUpdate,
InquilinoDelete,
inicio,
depto,
inquilino,
ganancias,
formulario_depto,
reserva_depto,
formulario_ganancia,
formulario_inquilino,
registro_ganancia,
registro_inquilino,
busqueda_inquilino,
buscar,
editar_inquilino, 
borrar_inquilino,
user_login,
user_register,
user_edit
)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= "Inicio"),

    path('depto/', depto, name="depto"),
    path('inquilino/', inquilino, name="inquilino"),
    path('ganancias/', ganancias, name="ganancias"),

    path('formulario_depto/',formulario_depto , name="formulario_depto"),
    path('lista_reserva/', reserva_depto , name="reserva_depto"),

    path('formulario_ganancia/', formulario_ganancia , name="formulario_ganancia"),
    path('lista_ganancia/', registro_ganancia , name="lista_ganancia"),

    path('formulario_inquilido/',formulario_inquilino , name="formulario_inquilino"),
    path('lista_inquilino/', registro_inquilino , name="lista_inquilino"),

    path('busqueda_inquilino/', busqueda_inquilino , name="busqueda_inquilino"),
    path('buscar/', buscar , name="buscar"),

    path('borrar_inquilino/<int:id>', borrar_inquilino , name="borrar_inquilino"),

    path('editarInquilino/<int:id>', editar_inquilino , name="editarInquilino"),

    path('inquilino-lista/', InquilinoList.as_view() , name="inquilino-lista"),
    path('inquilino-detalle/<pk>', InquilinoDetail.as_view() , name="inquilino-detalle"),
    path('inquilino-formulario/', InquilinoCreate.as_view() , name="inquilino-formulario"),
    path('inquilino-actualizar/<pk>', InquilinoUpdate.as_view() , name="inquilino-actualizar"),
    path('inquilino-delete/<pk>', InquilinoDelete.as_view() , name="inquilino-delete"),

    path('user-login/', user_login, name="user-login"),
    path('user-register/', user_register, name="user-register"),
    path('user-logout/', LogoutView.as_view(template_name = "user_logout.html") , name="user-logout"),
    path('user-edit/', user_edit , name="user-edit"),


    



]
