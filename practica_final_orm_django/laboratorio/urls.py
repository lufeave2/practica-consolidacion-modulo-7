from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_laboratorios, name='lista_laboratorios'),
    path('crear/', views.crear_laboratorio, name='crear_laboratorio'),
    path('editar/<int:id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
