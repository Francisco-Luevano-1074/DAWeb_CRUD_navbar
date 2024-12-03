from django.shortcuts import render, redirect
from .models import Gato

# Create your views here.

def Inicio_vistaGato(request):
    losgatos=Gato.objects.all()
    return render(request, 'gestionarGato.html', {'misgatos' : losgatos})

def registrargato(request):
    id_gato=request.POST['txtid_gato']
    id_venta=request.POST['txtid_venta']
    id_orden=request.POST['txtid_orden']
    nombre=request.POST['txtnombre']
    edad=request.POST['txtedad']
    color=request.POST['txtcolor']
    raza=request.POST['txtraza']
    precio=request.POST['txtprecio']
    caracteristica=request.POST['txtcaracteristica']

    guardargatos=Gato.objects.create(id_gato=id_gato, id_venta=id_venta, id_orden=id_orden, nombre=nombre, edad=edad, color=color,raza=raza,precio=precio,caracteristica=caracteristica)
    return redirect ("Gato")



def seleccionargato(request, id_gato):
    gato = Gato.objects.get(id_gato=id_gato)
    return render(request, "editarGato.html", {"misgatos": gato})


def editargato(request):
    if request.method == "POST":
        id_gato = request.POST['txtid_gato']
        try:
            gato = Gato.objects.get(id_gato=id_gato)
            gato.id_venta = request.POST['txtid_venta']
            gato.id_orden = request.POST['txtid_orden']
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



def borrargato(request,id_gato):
    gato=Gato.objects.get(id_gato=id_gato)
    gato.delete()
    return redirect("Gato")
