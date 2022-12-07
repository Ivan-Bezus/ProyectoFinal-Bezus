from django.urls import path

from EmpApp1.views import(
# InquilinoList,
# InquilinoDetail,
# InquilinoCreate, 
# InquilinoUpdate,
# InquilinoDelete,
inicio,
about_me,
contact_me,
booking_main,
booking_create,
booking_read,
booking_update,
booking_detail,
booking_delete,
person_main,
person_create,
person_read,
person_detail,
person_update,
person_delete,
gain_main,
gain_create,
gain_read,
gain_detail,
gain_update,
gain_delete,
# formulario_ganancia,
# formulario_inquilino,
# registro_ganancia,
# registro_inquilino,
# busqueda_inquilino,
# buscar,
# editar_inquilino, 
# borrar_inquilino,
user_login,
user_register,
user_edit
)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #URLS INICIO y ABOUT ME
    path('', inicio, name= "Inicio"),
    path('about-me/', about_me , name="about-me"),
    path('contact-me/', contact_me , name="contact-me"),

    #URLS PERSON
    path('person-main/', person_main, name="person-main"),
    path('person-create/',person_create.as_view(), name="person-create"),
    path('person-read/',person_read.as_view(), name="person-read"),
    path('person-detail/<pk>',person_detail.as_view(), name="person-detail"),
    path('person-update/<pk>',person_update.as_view(), name="person-update"),
    path('person-delete/<pk>',person_delete.as_view(), name="person-delete"),
 
    #URLS BOOKING
    path('booking-main/',booking_main, name="booking-main"),
    path('booking-create/',booking_create.as_view() , name="booking-create"),
    path('booking-read/',booking_read.as_view() , name="booking-read"),
    path('booking-detail/<pk>',booking_detail.as_view() , name="booking-detail"),
    path('booking-update/<pk>',booking_update.as_view() , name="booking-update"),
    path('booking-delete/<pk>',booking_delete.as_view(), name="booking-delete"),

    #URLS GAIN
    path('gain-main/', gain_main, name="gain-main"),
    path('gain-create/',gain_create.as_view() , name="gain-create"),
    path('gain-read/',gain_read.as_view() , name="gain-read"),
    path('gain-detail/<pk>',gain_detail.as_view() , name="gain-detail"),
    path('gain-update/<pk>',gain_update.as_view() , name="gain-update"),
    path('gain-delete/<pk>',gain_delete.as_view() , name="gain-delete"),

    #URLS USERS : Login, Logout, Register, Edit
    path('user-login/', user_login, name="user-login"),
    path('user-register/', user_register, name="user-register"),
    path('user-logout/', LogoutView.as_view(template_name = "user_logout.html") , name="user-logout"),
    path('user-edit/', user_edit , name="user-edit"),


    #URLS FUERA DE USO:
    # path('formulario_ganancia/', formulario_ganancia , name="formulario_ganancia"),
    # path('lista_ganancia/', registro_ganancia , name="lista_ganancia"),
    # path('formulario_inquilido/',formulario_inquilino , name="formulario_inquilino"),
    # path('lista_inquilino/', registro_inquilino , name="lista_inquilino"),
    # path('busqueda_inquilino/', busqueda_inquilino , name="busqueda_inquilino"),
    # path('buscar/', buscar , name="buscar"),
    # path('borrar_inquilino/<int:id>', borrar_inquilino , name="borrar_inquilino"),
    # path('editarInquilino/<int:id>', editar_inquilino , name="editarInquilino"),



]
