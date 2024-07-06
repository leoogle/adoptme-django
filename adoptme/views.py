# adoptme/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tienda(request):
    return render(request, 'tienda.html')

def donaciones(request):
    return render(request, 'donaciones.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')
