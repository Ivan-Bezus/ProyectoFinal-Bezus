from django.contrib import admin

from .models import Avatar, Booking, Person, Gain
# Register your models here.

admin.site.register(Person)
admin.site.register(Booking)
admin.site.register(Gain)
admin.site.register(Avatar)