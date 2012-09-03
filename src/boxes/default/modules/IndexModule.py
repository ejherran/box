# -*- coding: utf-8 -*-

# Modulo de entrada de la aplicación

from ice.service.module import Module

class IndexModule(Module):
    
    def __init__(self, request):
        Module.__init__(self, request);
    
    def indexAction(self, prm = []):
        self.openSession()
        self.content = "<h1>Sesion creada con exito</h1>"
        
        return self.responseHtml()
    
    def guardarAction(self, prm = []):
        self.content = "<b>Guardado:</b> "+prm[0]+' => '+prm[1]
        self.setVarSession(prm[0], prm[1])
        return self.responseHtml()
    
    def leerAction(self, prm = []):
        value = self.getVarSession(prm[0])
        
        if(value == None):
            value = 'None'
            
        self.content = "<b>Leido: </b>" + prm[0] + " => "+value 
        return self.responseHtml()  
    
    def borrarAction(self, prm = []):
        if(self.delVarSession(prm[0])):
            self.content = "<b>Borrado:</b> "+prm[0]
        else:
            self.content = "<b>Imposible Borarr: </b> "+prm[0]
        return self.responseHtml()
    
    def createTable(self, prm = []):
        xcon = self.dbMod()
        xcon.insert('test', {'id':0, 'data':'moto'})
        self.content = "<b>OK</b>"
        return self.responseHtml()