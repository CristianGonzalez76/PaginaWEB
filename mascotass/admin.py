from asyncore import read
from re import search
from django.contrib import admin
from .models import mascota, estadomascota
# Register your models here.

class mascotassAdmin(admin.ModelAdmin):
    list_display=('correlativo','nombre','created','updated')
    search_fields=('estado','nombre')
    list_filter=('raza','estado')

admin.site.register(mascota,mascotassAdmin)

class estadosmascotaAdmin(admin.ModelAdmin):
    list_display=('situacion','created','updated')
admin.site.register(estadomascota,estadosmascotaAdmin)

