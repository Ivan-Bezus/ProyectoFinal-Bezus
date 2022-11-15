from django.contrib import admin

from .models import Depto, Inquilino, Ganancia
# Register your models here.

admin.site.register(Depto)
admin.site.register(Inquilino)
admin.site.register(Ganancia)