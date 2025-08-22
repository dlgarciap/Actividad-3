from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('administradores/', views.administradores, name='administradores'),
]