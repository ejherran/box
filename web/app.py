#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fijar path de busqueda para paquetes 
import sys, os
path = os.path.dirname(__file__)
path = os.path.split(path)
sys.path.append(path[0])

# Importar componente para gestionar petición
from webob import Request

# Importar loader de ICE
from src.module.test import Test

def application(environ, start_response):
    
    request = Request(environ)
    
    res = ''
    
    try:
        a = float(request.params['a'])
        b = float(request.params['b'])
        res = a+b
    except:
        pass
    
    status = '200 OK'
    output = """
    <FORM ACTION=app METHOD=POST>
        <B>A:</B><input type=text name='a' size=33><BR>
        <B>B:</B><input type=text NAME='b' size=33><BR>
        <B>A+B = """+str(res)+""" </B><BR>
        <INPUT TYPE=SUBMIT VALUE="Send"><INPUT TYPE=RESET VALUE="Cancela">
    </FORM>
    """
    ts = Test()
    output += ts.hitYa()
    
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]