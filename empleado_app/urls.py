from django.urls import path
from empleado_app import views

urlpatterns = [
    path('Empleado', views.Inicio_vistaEmpleado, name='Empleado'),
    path('registrarempleado/', views.registrarempleado, name='registrarempleado'),
    path('editarempleado/', views.editarempleado, name='editarempleado'),
    path('seleccionarempleado/<int:id_empleado>/', views.seleccionarempleado, name='seleccionarempleado'),
    path('borrarempleado/<int:id_empleado>/', views.borrarempleado, name='borrarempleado'),
]