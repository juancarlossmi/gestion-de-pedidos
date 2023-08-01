from django.shortcuts import render
# importacion del objeto carro del archivo "carro/carro.py"
# from carro.carro import Carro

def home(request):
    # carro=Carro(request)
    return render(request, "proyectowebapp/home.html")

def politica(request):
    return render(request, "proyectowebapp/politica.html")

def aviso_legal(request):
    return render(request, "proyectowebapp/aviso_legal.html")

def politica_cookies(request):
    return render(request, "proyectowebapp/politica_cookies.html")