from django.urls import path
from venta_app import views

urlpatterns = [
    path('Venta',views.Inicio_vistaVenta, name='Venta'),
    path('registrarVenta/',views.RegistrarVenta, name='registrar_venta'),
    path('editarVenta/',views.editarVenta, name='editar_venta'),
    path('seleccionarVenta/<int:id_venta>/',views.SeleccionarVenta, name='seleccionar_venta'),
    path('borrarVenta/<int:id_venta>/',views.BorrarVenta, name='borrar_venta'),
]
