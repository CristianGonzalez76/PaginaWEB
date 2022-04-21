from pyexpat import model
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import cla
from matplotlib.style import context

from proyectorefugio.views import reportes

from django.views.generic import ListView, View

from mascotass.models import mascota

# Create your views here.
def mascotas(request):
    return render(request, "reportes/reportes.html",{"repostes": reportes})
