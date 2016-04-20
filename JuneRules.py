#-*- coding: UTF-8 -*-
'''
Created on 2015年5月7日

@author: joel
'''
from JuneGenerator import Randomint,RandomString,mk_moblie,\
                                        RandomStringWithIntSX,\
    RandomStringWithInt, mkIp, mkEmail, mkName, mkCity, mkID, mkChinese, mkMac,mk_datetime_specified,range_date
from JuneGenData import PATH_SEPARATOR
import random
import string
KIND_SEPARATOR = 'k'
KEY_DATA_SEPARATOR = '@'
def isCustomedKind(kindstr):
    assert isinstance(kindstr, (str,unicode)),'kindstr type:%s'%type(kindstr)
    for key in ('slist','ilist','irange','srange','dttlist','dtlist','idtrange','sdtrange','dttrange','dtrange'):
        if kindstr.startswith(key):
            return True
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
def rule_range(opcode,v):
    assert isinstance(v, (str,unicode)),'v is not str or unicode!'
    rule = getRuleFromString(opcode, v)
    p1,p2 = rule[1].split(',')
    if opcode.startswith('idt'):#int date
        return mk_daterange('int', rule)
    elif opcode.startswith('sdt'):#string date
        return mk_daterange('string', rule)
    elif opcode.startswith('dtt'):#datetime
        return mk_daterange('datetime', rule)
    elif opcode.startswith('dt'):#date
        return mk_daterange('date', rule)
    elif opcode.startswith('i'):
        return random.randint(long(p1),long(p2))
    elif opcode.startswith('s'):
        return str(random.randint(long(p1),long(p2)))
    else:
        return None
def rule_list(opcode,v):
    assert isinstance(v, (str,unicode)),'v is not str or unicode!'
    rule = getRuleFromString(opcode, v)
    plist = rule[1].split(',')
    if opcode.startswith('dtt'):#datetime
        return mk_daterange('datetime', rule)
    elif opcode.startswith('dt'):#date
        return mk_daterange('date', rule)
    if opcode.startswith('i'):
        return int(string.join(random.sample(plist,1)).replace(' ',''))
    elif opcode.startswith('s'):
        return string.join(random.sample(plist,1)).replace(' ','')
    else:
        return None

def mk_datelist(kind,rule):
        plist = rule[1].split(',')
        if kind =='datetime':
            return mk_datetime_specified(string.join(random.sample(plist,1)).replace(' ','')+'00000')
        elif kind == 'date':
            return mk_datetime_specified(string.join(random.sample(plist,1)).replace(' ','')+'00000')
    
def mk_daterange(kind,rule):
        p1,p2 = rule[1].split(',')
        if kind == 'int':
            return long(mk_date(p1, p2))
        if kind =='string':
            return str(mk_date(p1, p2))
        elif kind in 'datetime':
            return mk_datetime(p1,p2)
        elif kind in 'date':
            return mk_date(p1,p2)
def mk_date(left,right):
    return range_date(left,right)
def mk_datetime(left,right):
    datestring = range_date(left,right)
    return mk_datetime_specified(datestring)

def getRuleFromString(opcode,jstring):
        left = jstring.index(opcode)+len(opcode)+1
        right = jstring[left:].index(')')+left
        return (opcode,jstring[left:right])
          
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

def valish(jstr,e=KEY_DATA_SEPARATOR):
    return jstr.replace(e, '')
    
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
    ################Warning################
    all rules below must be impose on last key(dict),not list key
    namely,imposed on pathKind's last field
    '''
    rule_dict = {}
    raw_flag = False
    for k in rules_dict.keys():
        if k.strip().startswith(KEY_DATA_SEPARATOR):
            raw_flag = True
            break
    for k,v in rules_dict.items(): 
        rawdata,v = v.split(PATH_SEPARATOR)
        if raw_flag:
            if v == 'bool':
                rule_dict[valish(k)] = True if rawdata.lower() == 'true' else False
            elif v in ('int','str','null'):
                exestr = '%s("%s")'%(v,rawdata)
                rule_dict[valish(k)] = eval(exestr) if v.strip() != 'null' else None
            else:
                rule_dict[valish(k)] = rawdata
        elif k.endswith('@url'):
            k = k[:-4]
            pass
        elif k.endswith('@db'):
            k = k[:-3]
            pass
        elif v=='str' and k.endswith('@pre'):
            k = k[:-4]
            rule_dict[k] = rawdata+rule_RandomStringWithInt(1, 5)
        elif v=='str'  and k.endswith('@suf'):
            k = k[:-4]
            rule_dict[k] = rule_RandomStringWithInt(1, 5)+rawdata
        elif k.endswith('@'):
            k = k[:-1]
            if v == 'bool':
                rule_dict[k] = True if rawdata.lower() == 'true' else False
            else:
                exestr = '%s("%s")'%(v,rawdata)
                rule_dict[k] = eval(exestr) if v.strip() != 'null' else None
        elif isinstance(v, str) and v.startswith(KIND_SEPARATOR):
            type,start,end = v[1:].split(KIND_SEPARATOR)
            rule_dict[k] = Rules[type](start,end)
        elif v != None:
            if isinstance(v, (str,unicode)):
                v = v.lower()
                if v.startswith('idtrange'):
                    rule_dict[k] = rule_range('idtrange', v)
                elif v.startswith('sdtrange'):
                    rule_dict[k] = rule_range('sdtrange', v)
                elif v.startswith('dttrange'):
                    rule_dict[k] = rule_range('dttrange', v)
                elif v.startswith('dtrange'):
                    rule_dict[k] = rule_range('dtrange', v)
                elif v.startswith('dttlist'):
                    rule_dict[k] = rule_list('dttlist', v)
                elif v.startswith('dtlist'):
                    rule_dict[k] = rule_list('dtlist', v)
                elif v.startswith('irange'):
                    rule_dict[k] = rule_range('irange',v)
                elif v.startswith('srange'):
                    rule_dict[k] = rule_range('srange',v)
                elif v.startswith('ilist'):
                    rule_dict[k] = rule_list('ilist',v)
                elif v.startswith('slist'):
                    rule_dict[k] = rule_list('slist',v)
                #######################################
                elif v == 'int':
                    rule_dict[k] = random.randint(1,1000)
                elif v == 'bool':
                    rule_dict[k] = bool(random.randint(0,1))
                elif  v == 'null':
                    rule_dict[k] = None
                elif v == 'str':
                    rule_dict[k] = rule_RandomStringWithInt(1, 5)
                else:
                    rule_dict[k] = v
#                 else:# v == 'str':
#                     rule_dict[k] = rule_RandomStringWithInt(1, 10)
            
    return rule_dict