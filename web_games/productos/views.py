from django.shortcuts import render
from .models import Producto
# Create your views here.
def verProductos(request):
    producto = Producto.objects.all()
    return render(request,"productos.html",{"productos":producto})