from django.urls import path
from cliente_app import views

urlpatterns = [
    path('Cliente', views.Inicio_vistaCliente, name='Cliente'),
    path('registrarcliente/', views.registrarcliente, name='registrarcliente'),
    path('editarcliente/', views.editarcliente, name='editarcliente'),
    path('seleccionarcliente/<int:id_cliente>/', views.seleccionarcliente, name='seleccionarcliente'),
    path('borrarcliente/<int:id_cliente>/', views.borrarcliente, name='borrarcliente'),
]
