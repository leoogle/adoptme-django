from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProductForm
from .models import Product, Sale

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
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'iniciar_sesion.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    return render(request, 'iniciar_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
def add_product(request):
    if not request.user.is_admin:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def checkout(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        address = request.POST['address']
        product = get_object_or_404(Product, id=product_id)
        Sale.objects.create(product=product, user=request.user, quantity=quantity, address=address)
        return redirect('tienda')
    else:
        return render(request, 'checkout.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = ProductForm()
    return render(request, 'agregar_producto.html', {'form': form})