from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def Inicio_vistaCliente(request):
    losclientes=Cliente.objects.all()
    return render(request, 'gestionarCliente.html', {'misclientes' : losclientes})

def registrarcliente(request):
    id_cliente=request.POST['txtid_cliente']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']
    no_telefono=request.POST['txtno_telefono']
    email=request.POST['txtemail']
    
    guardarclientes=Cliente.objects.create(id_cliente=id_cliente, nombre=nombre, apellido=apellido, no_telefono=no_telefono,email=email)
    return redirect ("Cliente")



def seleccionarcliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"misclientes": cliente})


def editarcliente(request):
    if request.method == "POST":
        id_cliente = request.POST['txtid_cliente']
        try:
            cliente = Cliente.objects.get(id_cliente=id_cliente)
            cliente.nombre = request.POST['txtnombre']
            cliente.apellido = request.POST['txtapellido']
            cliente.no_telefono= request.POST['txtno_telefono']
            cliente.email = request.POST['txtemail']
            cliente.save()
        except Cliente.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Cliente")



def borrarcliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("Cliente")
