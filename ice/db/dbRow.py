# -*- coding: utf-8 -*-

import string
from db import Db

class DbRow:

    name = None
    fields = {}
    pk = []
    db = Db()
    
    def __init__(self, tablename):
        
        self.name = tablename
        campos = self.db.getTypes(self.name)
        
        for campo in campos:
            self.fields[campo[0]] = 'NULL'
            if campo[2] == 'PRI':
                self.pk.append(campo[0])
    
    
    def insert(self):
        self.db.insert(self.name, self.fields)
    
    
    def setValue(self, field, value):
        self.fields[field] = value
    
        
    def update(self):
        condition = []
        
        for p in self.pk:
            if type(self.fields[p]) == type ('s'):
                condition.append( p + ' = \'' + self.fields[p] + '\'')
            else:
                condition.append( p + ' = ' + self.fields[p] )
        
        cond = string.join(condition,' and ')
        self.db.update(self.name, self.fields, cond)
    
    
    def fillBy(self, condition):
        row = self.db.getRow(self.name,condition)
        c = 0
        for p in self.fields.keys():
            self.setValue(p,row[c])
            c = c + 1
    
    
    def concatValues(self,fields,conector):
        value = []
        for a in fields:
            value.append[a]
        return string.join(value,conector)
    
    
    def save(self):
        condition=[]
        for p in self.pk:
            condition.append(p + ' = \'' + self.fields[p] + '\'')
        if self.db.getData('select count(*) from ' + self.name + ' where ' + string.join(condition,' and ')):
            self.update()
        else:
            self.insert()