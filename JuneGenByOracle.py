#coding=utf-8
'''
Created on 2016年4月22日

@author: duqiong
'''
from sqlalchemy import *  
from sqlalchemy.sql import select  
from sqlalchemy.schema import *  
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
meta=MetaData()
class Data():
    def __init__(self,tbn,connstr,jecho=False):
        self.tbname = tbn
        self.db_engine = create_engine(connstr,echo=jecho)
        self.conn = self.db_engine.connect()
        self.t = Table(self.tbname,meta, autoload=True, autoload_with=self.db_engine) # 这句话就提供了一个表名，其他的，sqlalchemy都帮你做完了
    def exist(self,wstr):
        s=select([self.t]).where(text(wstr))
        result=self.conn.execute(s)
        for row in result:
            return True
        return False
    def jdelete(self,wstr):
        d = delete(self.t).where(text(wstr))
        self.conn.execute(d)
        return self
    def setTable(self,tablename):
        self.tbname = tablename
        self.t = Table(self.tbname,meta, autoload=True, autoload_with=self.db_engine) # 这句话就提供了一个表名，其他的，sqlalchemy都帮你做完了
        return self
    def getCertainField(self,tablename,fieldlist,jwhere='',arecord=False,empty=True,rownum=100,startnum=0):
        self.setTable(tablename)
        querytext = ''
#         print sorted(fieldlist)
        if empty:
            for field in sorted(fieldlist):
                querytext += '%s is not null'%(field.lower())+' and '
        querytext += '%s<rownum and rownum<%s'%(startnum,rownum)
        if jwhere:
            querytext += ' and '+jwhere
        s=select([self.t]).where(text(querytext))
        print s
        result=self.conn.execute(s)
        Rdict = {}
        Rlist = []
        exestr = '['
        for field in sorted(fieldlist):
            Rdict[field] = []
            exestr += 'row[self.t.c.%s]'%(field.lower())+','
        exestr = exestr[:-1]+']'
        for row in result:
            if arecord:
                for field,v in zip(sorted(fieldlist),eval(exestr)):
                    Rdict[field].append(v)
            else:
                Rlist.append(eval(exestr))
        result.close()
        if arecord:
            return Rdict
        else:
            return Rlist
        
    def query(self,fieldlist,queryString):
        Rdict ={}
        Rlist =[]
        result=self.conn.execute(queryString)
        exestr = '['
        for field in sorted(fieldlist):
            Rdict[field] = []
            exestr += 'row["%s"]'%(field.lower())+','
        exestr = exestr[:-1]+']'
        for row in result:
            Rlist.append(eval(exestr))
        result.close()
        return Rlist
        
    def getCertainField_1(self,fieldlist,jwhere='',arecord=False,empty=True,rownum=100):
        querytext = ''
        if empty:
            for field in sorted(fieldlist):
                querytext += '%s is not null'%(field.lower())+' and '
        querytext += 'rownum <%s'%rownum
        if jwhere:
            querytext += ' and '+jwhere
        s=select([self.t]).where(text(querytext))
        result=self.conn.execute(s)
        Rdict = {}
        Rlist = []
        exestr = '['
        for field in sorted(fieldlist):
            Rdict[field] = []
            exestr += 'row[self.t.c.%s]'%(field.lower())+','
        exestr = exestr[:-1]+']'
        for row in result:
            if arecord:
                for field,v in zip(sorted(fieldlist),eval(exestr)):
                    Rdict[field].append(v)
            else:
                Rlist.append(eval(exestr))
        result.close()
        if arecord:
            return Rdict
        else:
            return Rlist


def updateTable(con_string,tname,indict,wherestr):
    db_engine=create_engine(con_string,echo=True)  
    meta=MetaData() 
    t = Table(tname,meta, autoload=True, autoload_with=db_engine) # 这句话就提供了一个表名，其他的，sqlalchemy都帮你做完了
#     s=update(t).values({t.c.idcard:'23',t.c.realname:'22'})# 提供查询条件
    s=update(t).where(wherestr).values(indict)
    
    print s
    conn=db_engine.connect()  
    result=conn.execute(s)
    result.close()  
    
def updateTableWithonefield(con_string,tname,indict,wherestr):
    db_engine=create_engine(con_string,echo=True)  
    meta=MetaData() 
    t = Table(tname,meta, autoload=True, autoload_with=db_engine) # 这句话就提供了一个表名，其他的，sqlalchemy都帮你做完了
#     s=update(t).values({t.c.idcard:'23',t.c.realname:'22'})# 提供查询条件
    s=update(t).where(wherestr).values(indict)
    print s
    conn=db_engine.connect()  
    result=conn.execute(s)
    result.close()     

