from django.shortcuts import render, redirect
from .models import Orden

# Create your views here.

def Inicio_vistaOrden(request):
    lasordenes=Orden.objects.all()
    return render(request, 'gestionarOrden.html', {'misordenes' : lasordenes})

def registrarorden(request):
    id_orden=request.POST['txtid_orden']
    id_empleado=request.POST['txtid_empleado']
    id_cliente=request.POST['txtid_cliente']
    id_producto=request.POST['txtid_producto']
    id_mesa=request.POST['txtid_mesa']
    id_gato=request.POST['txtid_gato']
    productos=request.POST['txtproductos']
    mesa=request.POST['txtmesa']
    nom_cliente=request.POST['txtnom_cliente']
    tipo=request.POST['txttipo']
    costo=request.POST['txtcosto']
    hora=request.POST['txthora']

    guardarordenes=Orden.objects.create(id_orden=id_orden, id_empleado=id_empleado, id_cliente=id_cliente, id_producto=id_producto, id_mesa=id_mesa, id_gato=id_gato,productos=productos, mesa=mesa, nom_cliente=nom_cliente,tipo=tipo,costo=costo,hora=hora)
    return redirect ("Orden")




def seleccionarorden(request, id_orden):
    orden = Orden.objects.get(id_orden=id_orden)
    return render(request, "editarOrden.html", {"misordenes": orden})


def editarorden(request):
    if request.method == "POST":
        id_orden = request.POST['txtid_orden']
        try:
            orden = Orden.objects.get(id_orden=id_orden)
            orden.id_empleado=request.POST['txtid_empleado']
            orden.id_cliente=request.POST['txtid_cliente']
            orden.id_producto=request.POST['txtid_producto']
            orden.id_mesa=request.POST['txtid_mesa']
            orden.id_gato=request.POST['txtid_gato']
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



def borrarorden(request,id_orden):
    orden=Orden.objects.get(id_orden=id_orden)
    orden.delete()
    return redirect("Orden")