from django.shortcuts import render

from django.http import HttpResponse # es una clase que permite ejecutar un respuesta http 

def index(request):
    return HttpResponse("Hellor Word")