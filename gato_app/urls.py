from django.urls import path
from gato_app import views

urlpatterns = [
    path('Gato', views.Inicio_vistaGato, name='Gato'),
    path('registrargato/', views.registrargato, name='registrargato'),
    path('editargato/', views.editargato, name='editargato'),
    path('seleccionargato/<int:id_gato>/', views.seleccionargato, name='seleccionargato'),
    path('borrargato/<int:id_gato>/', views.borrargato, name='borrargato'),
]
