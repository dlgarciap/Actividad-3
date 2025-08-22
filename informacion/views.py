from django.shortcuts import render
from django.http import HttpResponse

def estudiantes(request):
    return HttpResponse("Listado de estudiantes - Módulo Principal")

def administradores(request):
    return HttpResponse("Listado de administradores - Módulo Principal")