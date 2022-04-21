from django import forms

class formulario_contacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)

    apellidos=forms.CharField(label="Apellidos")

    email=forms.EmailField(label="Email")

    asunto=forms.CharField(label="Asunto", max_length=25,required=True)

    Mensaje=forms.CharField(label="Mensaje", widget=forms.Textarea,required=True)

