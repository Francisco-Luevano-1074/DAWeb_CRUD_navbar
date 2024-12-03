from django.urls import path
from producto_app import views

urlpatterns = [
    path('Producto',views.Inicio_vistaProducto, name='Producto'),
    path('registrarproducto/',views.registrarproducto, name='registrarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('seleccionarproducto/<int:codigo>/',views.seleccionarproducto, name='seleccionarproducto'),
    path('borrarproducto/<int:codigo>/',views.borrarproducto, name='borrarproducto'),
]
