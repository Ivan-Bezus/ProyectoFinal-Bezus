from django.contrib import admin

from .models import Avatar, Depto, Inquilino, Ganancia
# Register your models here.

admin.site.register(Depto)
admin.site.register(Inquilino)
admin.site.register(Ganancia)
admin.site.register(Avatar)