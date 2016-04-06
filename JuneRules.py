#-*- coding: UTF-8 -*-
'''
Created on 2015年5月7日

@author: joel
'''
from JuneGenerator import Randomint,RandomString,mk_moblie,\
                                        RandomStringWithIntSX,\
    RandomStringWithInt, mkIp, mkEmail, mkName, mkCity, mkID, mkChinese, mkMac
import random
import copy
KIND_SEPARATOR = 'k'
def isCustomedKind(kindstr):
    assert isinstance(kindstr, (str,unicode)),'kindstr type:%s'%type(kindstr)
    num = 0
    start = 0
    index = kindstr.find(KIND_SEPARATOR)
    while index != -1:
        num += 1
        start = index+2
        index = kindstr.find(KIND_SEPARATOR,start)
    if num == 3:
        return True
    else:
        return False
def rule_mk_phone(start,end):
    return mk_moblie()
def rule_mkname(start,end):
    return mkName()
def rule_mk_id(start,end):
    return mkID(1)[0]  
def rule_mk_mac(start,end):
    return mkMac()  
def rule_mkip(start,end):
    return mkIp()  
def rule_mkemail(start,end):
    return mkEmail()  
def rule_RandomStringWithInt(start,end):
    rd = random.randint(int(start),int(end))
    return RandomStringWithInt(rd)  
def rule_RandomStringWithIntSX(start,end):
    rd = random.randint(int(start),int(end))
    return RandomStringWithIntSX(rd)   
def rule_RandomString(start,end):
    rd = random.randint(int(start),int(end))
    return RandomString(rd)  
def rule_Randomint(start,end):
    rd = random.randint(int(start),int(end))
    return int(Randomint(rd))   
def rule_mkChinese(start,end):
    rd = random.randint(int(start),int(end))
    return mkChinese(rd)  
def rule_mkcity(start,end):
    return mkCity()      
Rules = {
        't':rule_mk_phone,
        'n':rule_mkname,
        'id':rule_mk_id,
        'mac':rule_mk_mac,
        'ip':rule_mkip,
        'email':rule_mkemail,
        'is':rule_RandomStringWithInt,
        'isx':rule_RandomStringWithIntSX,
        's':rule_RandomString,
        'i':rule_Randomint,
        'chinses':rule_mkChinese,
        'city':rule_mkcity
        }

def genDataAccordingRules(rules_dict):
    '''
    k type k start k end
    
    type:
        t telephone
        i int
        is int string
        s string
        n name
        time time
        ############
        int
        null
        bool
        str
    '''
    rule_dict = copy.deepcopy(rules_dict)#必须深拷贝
    for k,v in rule_dict.items(): 
        if isinstance(v, str) and v.startswith('k'):
            type,start,end = v[1:].split('k')
#             print type,start,end
            rule_dict[k] = Rules[type](start,end)
        elif v != None:
            if isinstance(v, str) and v == 'str':
                rule_dict[k] = rule_RandomStringWithInt(1, 10)
            elif isinstance(v, str) and v == 'int':
                rule_dict[k] = random.randint(1,1000)
            elif isinstance(v, str) and v == 'bool':
                rule_dict[k] = bool(random.randint(0,1))
            elif isinstance(v, str) and v == 'null':
                rule_dict[k] = None
            else:
                rule_dict[k] = v
    return rule_dict