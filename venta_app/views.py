from django.shortcuts import render, redirect
from .models import Venta

# Create your views here.

def Inicio_vistaVenta(request):
    lasventas=Venta.objects.all()
    return render(request, 'gestionarventa.html', {'misventas' : lasventas})

def RegistrarVenta(request):
    codigo=request.POST['txtcodigo']
    empaque=request.POST['txtempaque']
    contenido=request.POST['txtcontenido']
    dir_cliente=request.POST['txtdir_cliente']
    tel_cliente=request.POST['txttel_cliente']
    nom_cliente=request.POST['txtnom_cliente']
    total=request.POST['txttotal']

    guardarventas=Venta.objects.create(codigo=codigo, empaque=empaque, contenido=contenido, dir_cliente=dir_cliente,tel_cliente=tel_cliente, nom_cliente=nom_cliente, total=total)
    return redirect ("Venta")




def SeleccionarVenta(request, codigo):
    venta = Venta.objects.get(codigo=codigo)
    return render(request, "editarVenta.html", {"misventas": venta})


def editarVenta(request):
    if request.method == "POST":
        codigo = request.POST['txtcodigo']
        try:
            venta = Venta.objects.get(codigo=codigo)
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



def BorrarVenta(request,codigo):
    venta=Venta.objects.get(codigo=codigo)
    venta.delete()
    return redirect("Venta")