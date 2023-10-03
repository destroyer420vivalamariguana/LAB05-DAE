from django.shortcuts import render

# Create your views here.

from .models import Categoria, Cliente, Producto

def index(request):
    categorias = Categoria.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {'categorias': categorias, 'clientes': clientes, 'productos': productos})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/categorias.html', {'categorias': categorias})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tienda/clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})
