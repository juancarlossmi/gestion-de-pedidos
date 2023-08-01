from django import forms

class Formulario_contacto(forms.Form):
    nombre=forms.CharField(label="nombre", max_length=50, required=True, error_messages={'required': 'Campo requerido'})
    email=forms.EmailField(label="email", max_length=50, required=True, error_messages={'required': 'Campo requerido'})
    # con attrs =  Agregamos la clase CSS al textarea
    contenido=forms.CharField(label="contenido", widget=forms.Textarea(attrs={'class':'contenido-textarea'}), required=True, error_messages={'required': 'Campo requerido'})