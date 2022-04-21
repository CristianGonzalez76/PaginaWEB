from django.shortcuts import render
from mascotass.models import mascota

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.
def mascotas(request):
    mascotas=mascota.objects.all()
    return render(request, "mascotas/mascotas.html",{"mascotas": mascotas})

