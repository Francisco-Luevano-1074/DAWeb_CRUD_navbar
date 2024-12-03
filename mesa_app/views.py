from django.shortcuts import render, redirect
from .models import Mesa

# Create your views here.

def Inicio_vistaMesa(request):
    lasmesas=Mesa.objects.all()
    return render(request, 'gestionarMesa.html', {'mismesas' : lasmesas})

def registrarmesa(request):
    id_mesa=request.POST['txtid_mesa']
    ubicacion=request.POST['txtubicacion']
    tamaño=request.POST['txttamaño']
    sillas=request.POST['txtsillas']
    id_gato=request.POST['txtid_gato']
    
    guardarmesas=Mesa.objects.create(id_mesa=id_mesa, ubicacion=ubicacion, tamaño=tamaño, sillas=sillas, id_gato=id_gato)
    return redirect ("Mesa")

def seleccionarmesa(request, id_mesa):
    mesa = Mesa.objects.get(id_mesa=id_mesa)
    return render(request, "editarMesa.html", {"mismesas": mesa})


def editarmesa(request):
    if request.method == "POST":
        id_mesa = request.POST['txtid_mesa']
        try:
            mesa = Mesa.objects.get(id_mesa=id_mesa)
            mesa.ubicacion = request.POST['txtubicacion']
            mesa.tamaño = request.POST['txttamaño']
            mesa.sillas= request.POST['txtsillas']
            mesa.id_gato=request.POST['txtid_gato']
            mesa.save()
        except Mesa.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Mesa")



def borrarmesa(request,id_mesa):
    mesa=Mesa.objects.get(id_mesa=id_mesa)
    mesa.delete()
    return redirect("Mesa")