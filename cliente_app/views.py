from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def Inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request, 'gestionarCliente.html', {'misclientes' : losclientes})

def registrarcliente(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    no_telefono=request.POST['txtno_telefono']
    email=request.POST['txtemail']
    
    guardarclientes=Cliente.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, no_telefono=no_telefono,email=email)
    return redirect ("Cliente")



def seleccionarcliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    return render(request, "editarCliente.html", {"misclientes": cliente})


def editarcliente(request):
    if request.method == "POST":
        codigo = request.POST['txtcodigo']
        try:
            cliente = Cliente.objects.get(codigo=codigo)
            cliente.nombre = request.POST['txtnombre']
            cliente.apellido = request.POST['txtapellido']
            cliente.no_telefono= request.POST['txtno_telefono']
            cliente.email = request.POST['txtemail']
            cliente.save()
        except Cliente.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Cliente")



def borrarcliente(request,codigo):
    cliente=Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect("Cliente")
