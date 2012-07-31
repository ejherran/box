# -*- coding: utf-8 -*-

# Gestor de carga de aplicaciones

import urllib2 as url
from webob import Response
from src.config.call import caller

def callMod(request):
    
    com = str(request.url);
    bas = str(request.application_url)
    cal = com.replace(bas, '')
    par = cal[1:].split('/')
    
    if(par[0] == ''):
        par = []
    
    p = 0
    while p < len(par):
        par[p] = url.unquote(str(par[p]).encode('utf8'))
        p += 1
    
    try:
        while len(par) < 2:
            par.append('index')
        
        caso = caller[par[0]]
        msg = "Modulo = "+caso['mod']+"<br>"
        msg += "Acción = "+caso[par[1]]+"<br>"
        msg += "Parametros = "+str(par[2:])        
    except:
        msg = "Acción no encontrada, verifique su petición: <b>"+cal+"</b> !"
    
    res = Response(body = msg, content_type = 'text/html')
    return res