from django.shortcuts import render
from servicios.models import servicio
# Create your views here.

def servicios(request):
    # servicios = obtenemos todos los serviios registrados por el admin del sitio
    servicios=servicio.objects.all()
    return render(request, "servicios/servicios.html",{"servicios": servicios})