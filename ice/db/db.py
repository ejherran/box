# -*- coding: utf-8 -*-

import MySQLdb as db
import string

class Db:
    
    connection = None
    engine = None
    host = None
    user = None
    password = None
    database = None
    sql = None                          #oci,pgsql,sqls
    
    
    def __init__(self, **params):
        
        if(params):
            self.engine = params['engine'] if 'engine' in params.keys() else 'mysql' 
            self.host = params['host'] if 'host' in params.keys() else 'localhost'
            self.user = params['user'] if 'user' in params.keys() else 'user'
            self.password = params['password'] if 'password' in params.keys() else 'password'
            self.database = params['database'] if 'database' in params.keys() else 'database'
        else:
            from src.config.db import ORMConfig as config
            self.engine = config.engine
            self.host = config.host
            self.user = config.user
            self.password = config.password
            self.database = config.database
        
        try:
            self.connection=db.connect(self.host,self.user,self.password,self.database)
            self.connection.close()
        except StandardError, e:
            print e
    
    
    def cntOpen(self):
        if self.engine == 'mysql':
            self.connection=db.connect(self.host,self.user,self.password,self.database)
    
    
    def cntClose(self):
        self.connection.close()
    
        
    def getRow(self,table,condition):
        self.sql='select * from ' + table + ' where ' + condition 
        if self.engine == 'mysql':
            self.sql += ' limit 0,1'
        return self.getArray(self.sql)
               
    
    def getTypes(self, table):
        if (self.engine=='mysql'):
            self.sql='desc ' + table
            rows = self.getArray(self.sql)                    
            p=[]
            for r in rows:
                p.append((r[0],r[1],r[3]))
        return p
    
    
    def query(self, sql):
        self.sql=sql
        self.cntOpen()
        self.execute()
        self.cntClose()
        
    
    def commit(self):
        self.connection.commit()
            
    
    def rollback(self):
        self.connection.rollback()
        
    
    def getArray(self,sql):
        self.cntOpen()
        self.sql=sql
        
        fetch = self.execute()
        self.cntClose()
        return fetch        
    
    
    def execute(self):
        self.sql = string.replace(self.sql, ';', '')
        cursor = self.connection.cursor()
        cursor.execute(self.sql)
        response = cursor.fetchall()
        cursor.close()
        self.commit()
        
        if(response == ()):
            response = None
        
        return response
    
    
    def insert(self, table, fields):
        
        satt = string.replace(str(fields.keys()), '[', '(')
        satt = string.replace(satt, ']', ')')
        satt = string.replace(satt, "'", "")
        
        sval = string.replace(str(fields.values()), '[', '(')
        sval = string.replace(sval, ']', ')')
        
        self.sql = 'insert into ' + str(table) + ' ' + satt + ' values ' + sval
        
        self.cntOpen()
        self.execute()
        self.cntClose()
    
    
    def update(self, table, fields, condition):
        
        self.sql = 'update ' + table + ' set '
        
        for key in fields.keys():
            if(type(fields[key]) == type('s')):
                tmp = '\''
            else:
                tmp = ''
            
            self.sql += key + '=' + tmp + str(fields[key])+ tmp + ', '
        
        
        self.sql = self.sql[:-2] + ' '
        self.sql += 'where '+str(condition)
        
        self.cntOpen()
        self.execute()
        self.cntClose()
    
    
    def getData(self, sql):
        self.sql = sql
        self.cntOpen()
        row = self.execute()
        data = row[0]
        self.cntClose()
        return data