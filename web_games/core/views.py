from django.shortcuts import render

# Create your views here.
def home(request):
    productos = []
    return render(request,"index.html",{'titulo':'hola nuestros productor son op','productos':productos})

def contacto(request):
    return render(request,"contacto.html")