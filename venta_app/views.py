from django.shortcuts import render, redirect
from .models import Venta

# Create your views here.

def Inicio_vistaVenta(request):
    lasventas=Venta.objects.all()
    return render(request, 'gestionarventa.html', {'misventas' : lasventas})

def RegistrarVenta(request):
    id_venta=request.POST['txtid_venta']
    id_empleado=request.POST['txtid_empleado']
    id_cliente=request.POST['txtid_cliente']
    id_producto=request.POST['txtid_producto']
    id_gato=request.POST['txtid_gato']
    fecha_venta=request.POST['txtfecha_venta']
    empaque=request.POST['txtempaque']
    contenido=request.POST['txtcontenido']
    dir_cliente=request.POST['txtdir_cliente']
    tel_cliente=request.POST['txttel_cliente']
    nom_cliente=request.POST['txtnom_cliente']
    total=request.POST['txttotal']

    guardarventas=Venta.objects.create(id_venta=id_venta, id_empleado=id_empleado, id_cliente=id_cliente, id_producto=id_producto, id_gato=id_gato, fecha_venta=fecha_venta, empaque=empaque, contenido=contenido, dir_cliente=dir_cliente,tel_cliente=tel_cliente, nom_cliente=nom_cliente, total=total)
    return redirect ("Venta")




def SeleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request, "editarVenta.html", {"misventas": venta})


def editarVenta(request):
    if request.method == "POST":
        id_venta = request.POST['txtid_venta']
        try:
            venta = Venta.objects.get(id_venta=id_venta)
            venta.id_empleado=request.POST['txtid_empleado']
            venta.id_cliente=request.POST['txtid_cliente']
            venta.id_producto=request.POST['txtid_producto']
            venta.id_gato=request.POST['txtid_gato']
            venta.fecha_venta=request.POST['txtfecha_venta']
            venta.empaque = request.POST['txtempaque']
            venta.contenido = request.POST['txtcontenido']
            venta.dir_cliente = request.POST['txtdir_cliente']
            venta.tel_cliente = request.POST['txttel_cliente']
            venta.nom_cliente = request.POST['txtnom_cliente']
            venta.total = request.POST['txttotal']
            venta.save()
        except Venta.DoesNotExist:
            # Manejo del error si la venta no existe
            pass
    return redirect("Venta")



def BorrarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("Venta")