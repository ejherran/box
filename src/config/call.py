# -*- coding: utf-8 -*-

## - Archivo de configuración de llamadas a modulos - ##

boxes = {}
modules = {}
methods = {} 

# Configuración de boxes
# boxes {'urlBox':'folderBox'}
boxes = {'index':'default'}

# configuración de modulos en cada box
# modules['urlBox'] = {'urlMod':'fileMod'}
modules['index'] = {'index':'IndexModule'}

# Configuración de metodos por cada modulo
# methods['urlBox'] = {'urlMod':{'urlMet':'methodName'}}
methods['index'] = {'index':{'index':'indexAction', 'guardar':'guardarAction', 'leer':'leerAction', 'borrar':'borrarAction'}}
