# -*- coding: utf-8 -*-

from dbRow import DbRow

class dbManager:
    
    primary = None
    slave = None
    fieldsrelations = None
    master = None
    detail = None
    rows = []
    
    def __init__(self, master, slave, relations):
        self.primary = master
        self.slave = slave
        self.fieldsrelations = relations
    
    
    def setMaster(self, fields):
        self.master = DbRow(self.primary)
        
        for p in fields.keys():
            self.master.setValue(p, fields[p])
    
    
    def addDetail(self,fields):
        detail = DbRow(self.slave)
        for p in fields.keys():
            detail.setValue(p,fields[p])        
        for a in self.fieldsrelations.keys():
            detail.fields[a] = self.master.fields[fields[a]]
        self.rows.append(detail)
    
    
    def updateData(self):
        self.master.save()
        for a in self.rows:
            a.save()