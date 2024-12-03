from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def Inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request, 'gestionarEmpleado.html', {'misempleados' : losempleados})

def registrarempleado(request):
    id_empleado=request.POST['txtid_empleado']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    no_telefono=request.POST['txtno_telefono']
    email=request.POST['txtemail']
    
    guardarempleados=Empleado.objects.create(id_empleado=id_empleado, nombre=nombre, apellido=apellido, no_telefono=no_telefono,email=email)
    return redirect ("Empleado")



def seleccionarempleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleado.html", {"misempleados": empleado})


def editarempleado(request):
    if request.method == "POST":
        id_empleado = request.POST['txtid_empleado']
        try:
            empleado = Empleado.objects.get(id_empleado=id_empleado)
            empleado.nombre = request.POST['txtnombre']
            empleado.apellido = request.POST['txtapellido']
            empleado.no_telefono= request.POST['txtno_telefono']
            empleado.email = request.POST['txtemail']
            empleado.save()
        except Empleado.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Empleado")



def borrarempleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("Empleado")

