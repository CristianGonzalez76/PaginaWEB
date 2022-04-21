from django.shortcuts import render, redirect

from .forms import formulario_solicitud

from django.core.mail import EmailMessage
# Create your views here.

def solicitud(request):
    formulario_contacto=formulario_solicitud()

    if request.method=="POST":
        formulario_contacto=formulario_solicitud(data=request.POST)
 
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            apellidos=request.POST.get("apellidos")
            email=request.POST.get("email")
            telefono=request.POST.get("telefono")
            edad=request.POST.get("edad")
            direccion=request.POST.get("direccion")
            contenido=request.POST.get("contenido")
            mascotas=request.POST.get("mascotas")

            email=EmailMessage("Nueva Solicitud de adopcion",
            "Nombre: {} {} \n Correo: {} \n Telefono: {} \n Edad: {} \n Direccion: {} \n Desea adoptar una mascota por: {} \n Posee mascotas: {}".format(nombre,apellidos,email,telefono,edad,direccion,contenido,mascotas),"",["refugiodemascotas.guatemala@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/solicitud/?valido")
            except:
                return redirect("/solicitud/?novalido")

            

    return render(request, "solicitud/solicitud.html",{'miformulario':formulario_contacto})
