import sys
import os
  
def fixPath(path):
    sys.path.append(path)

def getDirname(filePoint):
    return os.path.dirname(filePoint)

def dashPath(path, levels = 1):
    lvl = 0
    
    while(lvl < levels):
        path = os.path.split(path)
        path = path[0]
        
        lvl += 1
    
    return path

def plusPath(path, nextDir):
    path = os.path.join(path, nextDir)
    return path
