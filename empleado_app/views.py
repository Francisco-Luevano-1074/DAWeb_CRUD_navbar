from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def Inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request, 'gestionarEmpleado.html', {'misempleados' : losempleados})

def registrarempleado(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    no_telefono=request.POST['txtno_telefono']
    email=request.POST['txtemail']
    
    guardarempleados=Empleado.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, no_telefono=no_telefono,email=email)
    return redirect ("Empleado")



def seleccionarempleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    return render(request, "editarEmpleado.html", {"misempleados": empleado})


def editarempleado(request):
    if request.method == "POST":
        codigo = request.POST['txtcodigo']
        try:
            empleado = Empleado.objects.get(codigo=codigo)
            empleado.nombre = request.POST['txtnombre']
            empleado.apellido = request.POST['txtapellido']
            empleado.no_telefono= request.POST['txtno_telefono']
            empleado.email = request.POST['txtemail']
            empleado.save()
        except Empleado.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Empleado")



def borrarempleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    empleado.delete()
    return redirect("Empleado")

