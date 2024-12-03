from django.urls import path
from producto_app import views

urlpatterns = [
    path('Producto',views.Inicio_vistaProducto, name='Producto'),
    path('registrarproducto/',views.registrarproducto, name='registrarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('seleccionarproducto/<int:id_producto>/',views.seleccionarproducto, name='seleccionarproducto'),
    path('borrarproducto/<int:id_producto>/',views.borrarproducto, name='borrarproducto'),
]
