from django.urls import path
from mesa_app import views

urlpatterns = [
    path('Mesa', views.Inicio_vistaMesa, name='Mesa'),
    path('registrarmesa/', views.registrarmesa, name='registrarmesa'),
    path('editarmesa/', views.editarmesa, name='editarmesa'),
    path('seleccionarmesa/<int:id_mesa>/', views.seleccionarmesa, name='seleccionarmesa'),
    path('borrarmesa/<int:id_mesa>/', views.borrarmesa, name='borrarmesa'),
]
