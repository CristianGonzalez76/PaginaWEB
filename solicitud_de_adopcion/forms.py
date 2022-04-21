import email
from django import forms

class formulario_solicitud(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)

    apellidos=forms.CharField(label="Apellidos",required=True)

    email=forms.EmailField(label="Email", required=True)

    telefono=forms.CharField(max_length=8, required=True)

    edad=forms.IntegerField(label="Edad (años)", required=True)

    direccion=forms.CharField(label="Direccion (domiciliar)",max_length=100,required=True)

    contenido=forms.CharField(label="¿Por que desea adoptar?",max_length=200,required=True)

    mascotas=forms.CharField(label="¿Usted ya posee mascotas?", max_length=50)
