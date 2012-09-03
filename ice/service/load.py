# -*- coding: utf-8 -*-

## - Funciones para la carga dinamica de módulos - ##

# Carga de dependencias genericas
import urllib2 as url                                                               # Módulo para gestionar las url
from webob import Response                                                          # Módulo para gestiona respuestas como objetos

# Carga de dependecias internas
from src.config.call import boxes, modules, methods                                 # Módulo de configuración de rutas del proyecto

# Gestor de carga de aplicaciones
def callMod(request):
    
    com = str(request.url);                                                         # Obtiene la url de la petición ej: http://www.box.com/db/gestion/buscar/100
    bas = str(request.application_url)                                              # Obtiene la direccion base de la peticion ej: http://www.box.com/
    cal = com.replace(bas, '')                                                      # Obtiene los argumentos de invocación ej: /db/gestion/buscar/100
    par = cal[1:].split('/')                                                        # Genera una lista con los argumentos de invocación ej: ['db', 'gestion', 'buscar', '100']
    
    if(par[0] == ''):                                                               # Verifica que no sea una llamada vacia (sin argumentos) ej: http://www.box.com/
        par = []                                                                    # Limpia la lista de argumentos
    
    p = 0
    while p < len(par):                                                             # Codifica en formato utf8 los argumentos de la petición
        par[p] = url.unquote(str(par[p]).encode('utf8'))
        p += 1
    
    try:                                                                            # Idenficar e invocar la acción solicitada
        while len(par) < 3:                                                         # Verifica que no existan argumentos por defecto, en caso tal los completa con la llave 'index'
            par.append('index')
        
        box = boxes[par[0]]                                                         # Obtiene la caja solicitada según el primer arguemntos
        mod = modules[par[0]][par[1]]                                               # Obtiene el módulo solicitado según el segundo argumento
        met = methods[par[0]][par[1]][par[2]]                                       # Obtiene la acción solictada según el tercer argumento
        
        imp = loadImport('src.boxes.'+box+'.modules.'+mod)                          # Importa dinamicamente el modulo solicitado segun la ruta 'src.boxes.[box].modules.[mod]
        fun = loadMethod(imp, mod, met, request)                                    # Carga dinamicamente la funsión solictada del modulo importado
        
        res = fun(par[3:])                                                          # Invoca la función cargada, pasando como argumento una porción de la lista de invocación (del cuarto elemento en adelante), el resultado de la funsión queda en [res] que es un objeto Response
        
    except StandardError, e:                                                        # En caso de presentarse algún error
        res = "Error de ejecución, verifique su petición: <b>"+str(e)+"</b> !"      # Carga en [res] un mensaje de alerta y la descripccion del error.
        res = Response(body = res, content_type = 'text/html')                      # Crea un objeto respuesta
        
    return res                                                                      # Retorna el control al frontal de la applicación

# Importa dimanicamente un módulo de determinado paquete
# name: Nombre del paquete
def loadImport(name):
    
    mod = __import__(name)
    components = name.split('.')
    
    for comp in components[1:]:
        mod = getattr(mod, comp)
    
    return mod

# Carga una funcion de una clase especifica
# mod: Módulo que contiene la clase
# cla: Nombre de la clase a cargar
# fun: Nombre de la función a caragar
# req: Variable global que contiene la petición 
def loadMethod(mod, cla, fun, req = None):
    obj = getattr(mod, cla)       
    obj = obj(req)
    
    return getattr(obj, fun) 