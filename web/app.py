# -*- coding: utf-8 -*-

## - Punto de acceso a la aplicación, estadar WSGI - ##

# Fijar path de busqueda para paquetes 
import sys
import os

path = os.path.dirname(__file__)
path = os.path.split(path)
sys.path.append(path[0])

# Importar componente para gestionar petición
from webob import Request

# Importar loader de ICE
import ice.service.load as load

def application(environ, start_response):           # Punto de ingreso a la applicación, segun especificación WSGI
    
    request = Request(environ)                      # Crea el objeto [request] con los datos del entorno
    response = load.callMod(request)                # Crea el objeto [response] con los datos obtenidos al procesar la peticion [request]
    
    return response(environ, start_response)        # Envia la respuesta [response] al solicitante

