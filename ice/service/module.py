# -*- coding: utf-8 -*-

# Descriptor de modulos, clase padre

import string
from webob import Response                                                          # Módulo para gestiona respuestas como objetos
from ice.service import security
from ice.db.db import Db

class Module:
    
    req = None                                                                      # Objeto que contiene la petción
    res = None                                                                      # Objeto que contiene la respuesta
    content = None                                                                  # Variable de contenido de la respuesta
    strMod = string                                                                 # Objeto de acceso a los servicios de string
    secMod = security                                                               # Objeto de acceso a los servicios de seguridad
    dbMod = Db                                                                      # Objeto de acceso a los servicios de DB
    
    def __init__(self, request):
        self.req = request
        self.res = Response()
        
    def setBody(self, body):
        self.res.body = body;
    
    def setStatus(self, status):
        self.res.status = status
    
    def setContentType(self, ctype):
        self.res.content_type = ctype
    
    def responseHtml(self):
        self.setStatus('200 OK')
        self.setBody(self.content)
        self.setContentType('text/html')
        return self.res
    
    def responseText(self):
        self.setStatus('200 OK')
        self.setBody(self.content)
        self.setContentType('text/plain')
        return self.res
    
    def addCookie(self, key, value):
        self.res.set_cookie(key, value);
    
    def getSession(self):
        if('ICE-SESSION' in self.req.cookies):
            return self.req.cookies['ICE-SESSION']
        else:
            return None
    
    def haveSession(self):
        if(self.getSession() != None):
            return True
        else:
            return False
        
    def closeSession(self):
        session = self.getSession(); 
        if(session != None):
            self.secMod.deleteSession(session)
            
    def openSession(self):
        self.closeSession()
            
        key = self.secMod.createSession(self.req)
        self.addCookie('ICE-SESSION', key)
    
    def setVarSession(self, key, val):
        session = self.getSession()
        return self.secMod.writeInSession(session, key, val)
    
    def getVarSession(self, key):
        session = self.getSession()
        value = self.secMod.readInSession(session, key)
        
        return value
    
    def delVarSession(self, key):
        session = self.getSession()
        return self.secMod.deleteInSession(session, key)