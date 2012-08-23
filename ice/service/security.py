# -*- coding: utf-8 -*-

## - Funciones para el manejo de seguridad y sesiones - ##

import shelve

import os
import random
import time
import base64
import hashlib

import ice.service.directory as directory
from src.config.secure import ciclos, aleatorio, encode64

# Generar ID de sesion
def genKey():
    
    rnd = ''
    if(aleatorio):
        rnd = str(random.random())
        
    key = rnd + str(time.time())
    
    if(encode64):
        key = base64.b64encode(key)
    
    i = 0
    while(i < ciclos):
        has = hashlib.sha512()
        has.update(key)
        key = has.hexdigest()
        i += 1
    
    key = str(key).encode('utf8')
    key = key.upper()
    return key

def createSession(req):
    
    fileName = genKey() 
    
    sesion = shelve.open(getPathSession() + fileName + '.bsf');
    sesion.close()
    
    return fileName

def deleteSession(sessionFile):
    
    try:
        os.remove(getPathSession() + sessionFile + '.bsf')
        return True
    except:
        return False

def writeInSession(sessionFile, key, val):
    
    flag = True
    
    try:
        sesion = shelve.open(getPathSession() + sessionFile + '.bsf');
        sesion[key] = val
        sesion.close()
    except:
        flag = False
    
    return flag

def readInSession(sessionFile, key):
    
    val = None
    try:
        sesion = shelve.open(getPathSession() + sessionFile + '.bsf');
        val = sesion[key]
        sesion.close()
    except:
        pass
    
    return val

def deleteInSession(sessionFile, key):
    
    flag = True
    
    try:
        sesion = shelve.open(getPathSession() + sessionFile + '.bsf');
        del sesion[key]
        sesion.close()
    except:
        flag = False
    
    return flag

def getPathSession():
    
    boxPath = directory.dashPath(directory.getDirname(__file__), 2)
    filePath = directory.plusPath(boxPath, 'tmp/sessions/')
    
    return filePath    
    