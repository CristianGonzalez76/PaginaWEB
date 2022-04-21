
from django.shortcuts import redirect, render
from .forms import formulario_contacto
from django.core.mail import EmailMessage
# Create your views here.


def inde(request):
    FormularioContacto=formulario_contacto()

    if request.method=="POST":
        FormularioContacto=formulario_contacto(data=request.POST)
        if FormularioContacto.is_valid():
            nombre=request.POST.get("nombre")
            apellidos=request.POST.get("apellidos")
            email=request.POST.get("email")
            asunto=request.POST.get("asunto")
            mensaje=request.POST.get("Mensaje")

            email=EmailMessage("{}".format(asunto),
                "Nombre: {} {} \n Correo: {} \n Mensaje: {} ".format(nombre,apellidos,email,mensaje),"",["refugiodemascotas.guatemala@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/inde/?valido")
            except:
                return redirect("/inde/?novalido")



    return render(request, "inde/inde.html",{'miformulario':formulario_contacto})