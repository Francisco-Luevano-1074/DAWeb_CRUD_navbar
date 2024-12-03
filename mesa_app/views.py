from django.shortcuts import render, redirect
from .models import Mesa

# Create your views here.

def Inicio_vistaMesa(request):
    lasmesas=Mesa.objects.all()
    return render(request, 'gestionarMesa.html', {'mismesas' : lasmesas})

def registrarmesa(request):
    codigo=request.POST['txtcodigo']
    ubicacion=request.POST['txtubicacion']
    tamaño=request.POST['txttamaño']
    sillas=request.POST['txtsillas']
    
    guardarmesas=Mesa.objects.create(codigo=codigo, ubicacion=ubicacion, tamaño=tamaño, sillas=sillas)
    return redirect ("Mesa")

def seleccionarmesa(request, codigo):
    mesa = Mesa.objects.get(codigo=codigo)
    return render(request, "editarMesa.html", {"mismesas": mesa})


def editarmesa(request):
    if request.method == "POST":
        codigo = request.POST['txtcodigo']
        try:
            mesa = Mesa.objects.get(codigo=codigo)
            mesa.ubicacion = request.POST['txtubicacion']
            mesa.tamaño = request.POST['txttamaño']
            mesa.sillas= request.POST['txtsillas']
            mesa.save()
        except Mesa.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Mesa")



def borrarmesa(request,codigo):
    mesa=Mesa.objects.get(codigo=codigo)
    mesa.delete()
    return redirect("Mesa")