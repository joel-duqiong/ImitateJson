#coding=utf-8
'''
Created on 2016年4月22日

@author: duqiong
'''
from JuneGenByOracle import Data
from threading import current_thread
import thread
import operator
import random

GD_LOCK = thread.allocate_lock()
DB_SEPARATOR = '|'
TOTAL = 100
INDEX_MANAGE = {}

class GenDatabase():
    DatabaseMap = {}
    
    @staticmethod
    def add(jstr):
        GD_LOCK.acquire() 
        try:
            constr,tf = jstr.split(DB_SEPARATOR)
            if constr not in GenDatabase.DatabaseMap.keys():
                GenDatabase.DatabaseMap[constr] = {}
            t = current_thread()
            if t.ident not in GenDatabase.DatabaseMap[constr].keys():
                GenDatabase.DatabaseMap[constr][t.ident] = {}
            tname,field = tf.split('.')
            if tname not in GenDatabase.DatabaseMap[constr][t.ident].keys():
                GenDatabase.DatabaseMap[constr][t.ident][tname] = set()
            GenDatabase.DatabaseMap[constr][t.ident][tname].add(field)
            if 'connection' not in GenDatabase.DatabaseMap[constr].keys():
                GenDatabase.DatabaseMap[constr]['connection'] = Data(tname,constr)
        except Exception as ex:
            print ex
            GD_LOCK.release()
        else:
            GD_LOCK.release()
    @staticmethod
    def getData(constr,tname,rownum):
#         constr,tf = jstr.split(DB_SEPARATOR)
#         tname,field = tf.split('.')
        t = current_thread()
        connection = GenDatabase.DatabaseMap[constr]['connection']
        result = connection.getCertainField(tname,GenDatabase.DatabaseMap[constr][t.ident][tname], arecord=False,rownum=rownum)
        del GenDatabase.DatabaseMap[constr][t.ident][tname]
        return result

def fill(obj,constrs):
#     print constrs
    t = current_thread()
    for constr,v in constrs.items():
        for tname,kvs in v.items():
            result = GenDatabase.getData(constr, tname,TOTAL)
            index = -1
            old_key = ''
            print result
            try:
                tn_values = result[INDEX_MANAGE[constr][t.ident][tname]]
            except Exception as ex:
                INDEX_MANAGE[constr][t.ident][tname] = 0
                tn_values = result[INDEX_MANAGE[constr][t.ident][tname]]
            for k,v in sorted(kvs.items(),key=operator.itemgetter(1)):
                if v != old_key:
                    index += 1
#                 print INDEX_MANAGE[constr][t.ident][tname],index
#                 print result
                obj[k] = tn_values[index]
                old_key = v
            INDEX_MANAGE[constr][t.ident][tname] += 1
        t = current_thread()
        del GenDatabase.DatabaseMap[constr][t.ident]#防止内存泄漏
    
            
def generator(obj):
    constrs = {}
    for k,v in obj.items(): 
        if k.endswith('@db'):
            constr,tf = v.split('|')
            if constr not in constrs.keys():
                constrs[constr] = {}
            if constr not in INDEX_MANAGE.keys():
                INDEX_MANAGE[constr] = {}
            t = current_thread()
            if t.ident not in INDEX_MANAGE[constr].keys():
                INDEX_MANAGE[constr][t.ident] = {}#切记在django中发释放
            tname,field = tf.split('.')
            if tname not in constrs[constr].keys():
                constrs[constr][tname] = {}
            if tname not in INDEX_MANAGE[constr][t.ident].keys():
                INDEX_MANAGE[constr][t.ident][tname] = 0
            kk = k[:-3]
            constrs[constr][tname][kk] = field
#             print obj[k]
            GenDatabase.add(obj[k])
#             print obj
            del obj[k]
            obj[kk] = None
#     print GenDatabase.DatabaseMap
    fill(obj,constrs)