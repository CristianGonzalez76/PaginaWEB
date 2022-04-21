from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request, "proyectorefugio/home.html")


def reportes(request):
    return render(request, "proyectorefugio/reportes.html")



