# -*- coding: utf-8 -*-

from webob import Response                                                          # Módulo para gestiona respuestas como objetos
import ice.service.security as sc
import string


class IndexModule:
    
    req = None
    base = ""
    
    def __init__(self, request):
        self.req = request
        self.base = "Hola: "
    
    def indexAction(self, prm = []):
        msg = []
        for p in prm:
            msg.append(str(p))
        msg = string.join(msg, ',')
        
        self.req.environ['ICE-session'] = "Prueba De Sessión"
        
        key = sc.genKey()
        res = Response(body = key, content_type = 'text/html')
        res.set_cookie("ice-session", key)
        return res
    
    def venderAction(self, prm = []):
        res = "Sus cookies son: "+str(self.req.cookies)
        return Response(body = res, content_type = 'text/html') 
    
    def multiplica(self, msg):
        return msg*3