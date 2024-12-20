from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def Inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request, 'gestionarProducto.html', {'misproductos' : losproductos})

def registrarproducto(request):
    id_producto=request.POST['txtid_producto']
    nombre=request.POST['txtnombre']
    proveedor=request.POST['txtproveedor']
    cantidad=request.POST['txtcantidad']
    peso=request.POST['txtpeso']
    tamaño_empaque=request.POST['txttamaño_empaque']
    costo=request.POST['txtcosto']

    guardarproductos=Producto.objects.create(id_producto=id_producto, nombre=nombre, proveedor=proveedor, cantidad=cantidad,peso=peso,tamaño_empaque=tamaño_empaque,costo=costo)
    return redirect ("Producto")



def seleccionarproducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misproductos": producto})


def editarproducto(request):
    if request.method == "POST":
        id_producto = request.POST['txtid_producto']
        try:
            producto = Producto.objects.get(id_producto=id_producto)
            producto.nombre = request.POST['txtnombre']
            producto.proveedor = request.POST['txtproveedor']
            producto.cantidad= request.POST['txtcantidad']
            producto.peso = request.POST['txtpeso']
            producto.tamaño_empaque = request.POST['txttamaño_empaque']
            producto.costo = request.POST['txtcosto']
            producto.save()
        except Producto.DoesNotExist:
            # Manejo del error si el cliente no existe
            pass
    return redirect("Producto")



def borrarproducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("Producto")
