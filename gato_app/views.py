from django.shortcuts import render, redirect
from .models import Gato

# Create your views here.

def Inicio_vistaGato(request):
    losgatos=Gato.objects.all()
    return render(request, 'gestionarGato.html', {'misgatos' : losgatos})

def registrargato(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    edad=request.POST['txtedad']
    color=request.POST['txtcolor']
    raza=request.POST['txtraza']
    precio=request.POST['txtprecio']
    caracteristica=request.POST['txtcaracteristica']

    guardargatos=Gato.objects.create(codigo=codigo, nombre=nombre, edad=edad, color=color,raza=raza,precio=precio,caracteristica=caracteristica)
    return redirect ("Gato")



def seleccionargato(request, codigo):
    gato = Gato.objects.get(codigo=codigo)
    return render(request, "editarGato.html", {"misgatos": gato})


def editargato(request):
    if request.method == "POST":
        codigo = request.POST['txtcodigo']
        try:
            gato = Gato.objects.get(codigo=codigo)
            gato.nombre = request.POST['txtnombre']
            gato.edad = request.POST['txtedad']
            gato.color= request.POST['txtcolor']
            gato.raza = request.POST['txtraza']
            gato.precio = request.POST['txtprecio']
            gato.caracteristica = request.POST['txtcaracteristica']
            gato.save()
        except Gato.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Gato")



def borrargato(request,codigo):
    gato=Gato.objects.get(codigo=codigo)
    gato.delete()
    return redirect("Gato")
