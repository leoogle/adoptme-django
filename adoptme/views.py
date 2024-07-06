from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProductForm
from .models import Product, Sale

def home(request):
    return render(request, 'home.html')

def tienda(request):
    products = Product.objects.all()
    cart_items = request.session.get('cart', [])
    return render(request, 'tienda.html', {'products': products, 'cart_items': cart_items})

def donaciones(request):
    return render(request, 'donaciones.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

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
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)
    total = sum(product.price for product in products)
    return render(request, 'checkout.html', {'products': products, 'total': total})


@login_required
def agregar_producto(request):
    if not request.user.is_admin:
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = ProductForm()
    return render(request, 'agregar_producto.html', {'form': form})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', [])
    cart.append(product.pk)
    request.session['cart'] = cart
    return redirect('tienda')