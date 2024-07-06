from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ProductForm
from .models import Product, Cart, CartProduct

def home(request):
    return render(request, 'home.html')

def tienda(request):
    products = Product.objects.all()
    return render(request, 'tienda.html', {'products': products})

def donaciones(request):
    return render(request, 'donaciones.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'iniciar_sesion.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'iniciar_sesion.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = ProductForm()
    return render(request, 'agregar_producto.html', {'form': form})

def checkout(request):
    if request.method == 'POST':
        # Lógica para procesar la compra
        pass
    return render(request, 'checkout.html')