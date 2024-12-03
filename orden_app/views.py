from django.shortcuts import render, redirect
from .models import Orden

# Create your views here.

def Inicio_vistaOrden(request):
    lasordenes=Orden.objects.all()
    return render(request, 'gestionarOrden.html', {'misordenes' : lasordenes})

def registrarorden(request):
    codigo=request.POST['txtcodigo']
    id_empleado=request.POST['txtid_empleado']
    id_cliente=request.POST['txtid_cliente']
    id_producto=request.POST['txtid_producto']
    id_mesa=request.POST['txtid_mesa']
    productos=request.POST['txtproductos']
    mesa=request.POST['txtmesa']
    nom_cliente=request.POST['txtnom_cliente']
    tipo=request.POST['txttipo']
    costo=request.POST['txtcosto']
    hora=request.POST['txthora']

    guardarordenes=Orden.objects.create(codigo=codigo, id_empleado=id_empleado, id_cliente=id_cliente, id_producto=id_producto, id_mesa=id_mesa,productos=productos, mesa=mesa, nom_cliente=nom_cliente,tipo=tipo,costo=costo,hora=hora)
    return redirect ("Orden")




def seleccionarorden(request, codigo):
    orden = Orden.objects.get(codigo=codigo)
    return render(request, "editarOrden.html", {"misordenes": orden})


def editarorden(request):
    if request.method == "POST":
        codigo = request.POST['txtcodigo']
        try:
            orden = Orden.objects.get(codigo=codigo)
            orden.id_empleado=request.POST['txtid_empleado']
            orden.id_cliente=request.POST['txtid_cliente']
            orden.id_producto=request.POST['txtid_producto']
            orden.id_mesa=request.POST['txtid_mesa']
            orden.productos = request.POST['txtproductos']
            orden.mesa = request.POST['txtmesa']
            orden.nom_cliente= request.POST['txtnom_cliente']
            orden.tipo = request.POST['txttipo']
            orden.costo = request.POST['txtcosto']
            orden.hora = request.POST['txthora']
            orden.save()
        except Orden.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Orden")



def borrarorden(request,codigo):
    orden=Orden.objects.get(codigo=codigo)
    orden.delete()
    return redirect("Orden")