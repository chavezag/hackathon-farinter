from django.urls import path
from . import views

urlpatterns = [
    # Endpoints básicos
    path('', views.inicio, name='inicio'),
    path('salud/', views.salud, name='salud'),
    
    # TODO: Implementar estos endpoints para tareas
    path('tareas/', views.listar_tareas, name='listar_tareas'),
    path('tareas/<str:tarea_id>/', views.obtener_tarea, name='obtener_tarea'),
    
    # Para POST, PUT, PATCH, DELETE necesitas manejar en las vistas
    # ya que Django no distingue por método en las URLs
]