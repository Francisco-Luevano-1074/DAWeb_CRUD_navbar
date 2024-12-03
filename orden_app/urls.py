from django.urls import path
from orden_app import views

urlpatterns = [
    path('Orden', views.Inicio_vistaOrden, name='Orden'),
    path('registrarorden/', views.registrarorden, name='registrarorden'),
    path('editarorden/', views.editarorden, name='editarorden'),
    path('seleccionarorden/<int:codigo>/', views.seleccionarorden, name='seleccionarorden'),
    path('borrarorden/<int:codigo>/', views.borrarorden, name='borrarorden'),
]
