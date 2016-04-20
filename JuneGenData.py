#-*- coding: UTF-8 -*-
'''
Created on 2015年6月19日

@author: joel
'''
PATH_SEPARATOR = '/'
def covert2int(jstr):
    try:
        jstr = int(jstr)
    except Exception as ex:
        pass
    return jstr

def cmplist(x,y):
    '''
    custumed comparation of two lists
    '''
    x = [covert2int(xx) for xx in x.split('/')]
    y = [covert2int(yy) for yy in y.split('/')]
    return cmp(x,y)

def getEvenindex(ls):
    '''
    获取列表偶数下标
    '''
    Rls = []
    for i in zip(filter(lambda x :not x%2,xrange(len(ls))),filter(lambda x :x%2,xrange(len(ls)))):
        Rls.append(i)
    return Rls

def genDataByRulesPath(tdict):
    rdict = {}
    sortedkey = sorted(tdict,cmp=cmplist)
    for k,v in zip(sortedkey,[tdict[v] for v in sortedkey]):
        if isinstance(k, str) and PATH_SEPARATOR in k:
            tls = k.split(PATH_SEPARATOR)
            tls.append(v)
            glength = len(tls)/2 - 1
            cur_exestr = 'rdict' 
            for keyindex,kindindex in getEvenindex(tls):
                kind_exestr = 'isinstance(%s,dict)' %(cur_exestr)
                kind_exestr1 = 'isinstance(%s,list)' %(cur_exestr)
#                 print kind_exestr,cur_exestr
                if eval(kind_exestr):#dict
                    has_exestr = cur_exestr+'.has_key("%s")'%(tls[keyindex])
                    if not eval(has_exestr):#dict
                        if glength == 0:
                            if isinstance(tls[kindindex], str):
                                tmp_exestr = cur_exestr+'["'+tls[keyindex]+'"]="%s"'%(tls[kindindex])
                            else:
                                tmp_exestr = cur_exestr+'["'+tls[keyindex]+'"]=%s'%(tls[kindindex])
                        elif isinstance(tls[kindindex], str) and tls[kindindex].lower() == 'list':
                            tmp_exestr =cur_exestr+'["'+tls[keyindex]+'"]=[]'
                        elif isinstance(tls[kindindex], str) and tls[kindindex].lower() == 'dict':
                            tmp_exestr =cur_exestr+'["'+tls[keyindex]+'"]={}'
                        exec(tmp_exestr)
                        cur_exestr += '["'+tls[keyindex]+'"]'
                    else:
                        cur_exestr += '["'+tls[keyindex]+'"]'
                    
                elif eval(kind_exestr1):#list
                    index = 0
                    if isinstance(tls[keyindex], str) and tls[keyindex].lower() != 'none':
                        index = int(tls[keyindex])
                    len_exestr = 'len(%s)'%(cur_exestr)
                    length = eval(len_exestr)
                    if isinstance(tls[kindindex], str) and tls[kindindex].lower() == 'none' and length == 0:
                        index = 0
                    if index >= length:
                        if glength == 0:
                            if isinstance(tls[kindindex], str):
                                tmp_exestr = cur_exestr+'.append("%s")'%(tls[kindindex])
                            else:
                                tmp_exestr = cur_exestr+'.append(%s)'%(tls[kindindex])
                        elif isinstance(tls[kindindex], str) and tls[kindindex].lower() == 'list':
                            if length == 0:
                                tmp_exestr =cur_exestr+'[append([])'
                            else:
                                tmp_exestr =cur_exestr+'[append([])'
                        elif isinstance(tls[kindindex], str) and tls[kindindex].lower() == 'dict':
                            tmp_exestr =cur_exestr+'.append({})'
                        exec(tmp_exestr)
                        cur_exestr += '['+str(index)+']'
                    else:
                        cur_exestr += '['+str(index)+']'
                else:
                    pass
                glength -= 1
        else:
            rdict[k]=v
    return rdict