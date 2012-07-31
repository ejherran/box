'''
Created on 31/07/2012

@author: zero
'''

from ice.type.integer import Integer

class Load:
    msg = "Hello ICE"
    
    def getMsg(self):
        myint = Integer()
        return self.msg+' - '+myint.whatIs()