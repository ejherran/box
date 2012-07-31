# -*- coding: utf-8 -*-

# Fijar path de busqueda para paquetes 
import sys, os
path = os.path.dirname(__file__)
path = os.path.split(path)
sys.path.append(path[0])

# Importar componente para gestionar petición
from webob import Request

# Importar loader de ICE
import ice.service.load as load

def application(environ, start_response):
    
    request = Request(environ)
    response = load.callMod(request)
    
    return response(environ, start_response)