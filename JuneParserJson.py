#coding=utf-8
'''
Created on 2016年4月1日

@author: duqiong
'''
import json
from JuneRules import isCustomedKind
from JuneGenData import PATH_SEPARATOR,vanishSlash
import re
import random
LISTRANGE = re.compile('@\d*-\d*$')
class ParserJson(object):
    def parser_dict(self,prefix,indict,customedkind,withkind=True):
        for key in indict.keys():
            current_prefix = prefix
            current_prefix += PATH_SEPARATOR+'dict'+PATH_SEPARATOR+key
            if isinstance(indict[key],dict):
                self.parser_dict(current_prefix,indict[key],customedkind,withkind)
            elif isinstance(indict[key], list):
                self.parser_list(current_prefix,indict[key],customedkind,withkind)
            else:
                self.append(current_prefix, indict[key], customedkind, withkind)
                
    def parser_list(self,prefix,inlist,customedkind,withkind=True):
        i = -1
        for l in inlist:
            i += 1
            current_prefix = prefix
            current_prefix += PATH_SEPARATOR+'list'+PATH_SEPARATOR+str(i)
            if isinstance(l,dict):
                self.parser_dict(current_prefix,l,customedkind,withkind)
            elif isinstance(l, list):
                self.parser_list(current_prefix,l,customedkind,withkind)
            else:
                self.append(current_prefix, l, customedkind, withkind)
    
    def GenNodePaths(self,obj,customedkind=True,withkind=True):
        if isinstance(obj,str):
            obj = self.dictify(obj)
        assert isinstance(obj, dict),'so far do not support list json!'
        self.paths = []
        for key in obj.keys():
            if isinstance(obj[key],dict):
                self.parser_dict(key,obj[key],customedkind,withkind)
            elif isinstance(obj[key], list):
                self.parser_list(key,obj[key],customedkind,withkind)
            else:
                self.append(key, obj[key], customedkind, withkind)
        return self.paths
    
    def GetPathKind(self,obj,customedkind=True,withkind=True):
        '''
        obj: must be the type of dict or jsonstr
        customekind:stands for whether to support customed kind
        withkind: stands for whether to return pathKind with kind
        '''
        rdict = {}
        paths = self.GenNodePaths(obj,customedkind, withkind=withkind)
        for path in paths:
#             separated_index = path.rfind(PATH_SEPARATOR)
#             kind = path[separated_index+1:]
            k_separated_index = path.rfind(PATH_SEPARATOR)
            p_separated_index = path[:k_separated_index].rfind(PATH_SEPARATOR)#倒数第二个,即最后两：原数_类型
            kind = path[p_separated_index+1:]#原数_类型
            path = path[:p_separated_index]
            rdict[path] = kind
        return rdict
    
    def append(self,prefix,obj,customedkind,withkind):
#         print prefix,obj
        if isinstance(obj, str) or isinstance(obj, unicode):
            if PATH_SEPARATOR in obj:
                obj = vanishSlash(obj)
            if customedkind and isCustomedKind(obj):
                self.paths.append(prefix+(PATH_SEPARATOR+obj+PATH_SEPARATOR+obj if withkind else ''))
            else:
                self.paths.append(prefix+(PATH_SEPARATOR+obj+PATH_SEPARATOR+'str' if withkind else ''))
        elif isinstance(obj,bool):
            self.paths.append(prefix+(PATH_SEPARATOR+str(obj)+PATH_SEPARATOR+'bool' if withkind else ''))
        elif isinstance(obj,(int,long,float)):
            self.paths.append(prefix+(PATH_SEPARATOR+str(obj)+PATH_SEPARATOR+'int' if withkind else ''))
        elif obj is None:
            self.paths.append(prefix+(PATH_SEPARATOR+str(obj)+PATH_SEPARATOR+'null' if withkind else ''))
        else:
            raise Exception("append:%s"%prefix)
    def postConvert(self,obj,customedkind=True,withkind=True):
        '''
        called after GetPathKind to tackle pathrules'conversion
        to best
        '''
        pk = self.GetPathKind(obj, customedkind, withkind)
        print pk
        return pk
    def preConvert(self,obj,customedkind=True,withkind=True):
        '''
        called after GetPathKind to tackle pathrules'conversion
        '''
        if isinstance(obj,str):
            obj = self.dictify(obj)
        assert isinstance(obj, dict),'so far do not support list json!'
        self.enlargeConvert(obj)
        pk = self.GetPathKind(obj, customedkind, withkind)
        return pk
    def enlargeConvert(self,obj):
        def _enlarge(obj,k,v):
            del obj[k]
            k = k.split('@')[0]
            obj[k] = []
            if len(v)>0:
                for i in xrange(rd):
                    obj[k].append(v) 
        if isinstance(obj, list):
            for index,v in enumerate(obj):
                obj[index] = self.enlargeConvert(v)
        elif isinstance(obj, dict):
            for key,value in obj.items():
                flag,start,end = isListRangKey(key)
                if isinstance(value, list):
                    rd = random.randint(start,end)
#                     tmp = value[random.randint(0,len(value))]
                    tmp = value[0]
                    self.enlargeConvert(tmp)
                    if flag:
                        _enlarge(obj,key,tmp)
                else:
                    self.enlargeConvert(value)
             
    def dictify(self,jstr):
        assert isinstance(jstr,str),'jstr is not the type of str!'
        return self.convert(json.loads(jstr))
    
    @staticmethod
    def convert(dct):
        if isinstance(dct, dict):
            return {ParserJson.convert(key): ParserJson.convert(value) for key, value in dct.iteritems()}
        elif isinstance(dct, list):
            return [ParserJson.convert(element) for element in dct]
        elif isinstance(dct, unicode):
            return dct.encode('utf-8')
        else:
            return dct
def isListRangKey(jstr):
    assert isinstance(jstr, (str,unicode)),'jstr is not str or unicode!'
    m = LISTRANGE.findall(jstr)
    if len(m)==1:
        start,end = m[0][1:].split('-')
        if long(start)<long(end):
            return True,long(start),long(end)
        else:
            return  False,-1,-1
    else:
        return  False,0,0
if __name__ == '__main__':
    j = '{"soItemDtoList": [{"productId": [{"a":[{"aa":"june"},2,3]}]}, {"count": "FBIbCMNm"}],"ddd":123,"dfd":"ddf","boolv":true,"nullv":null}'
    ps = ParserJson()
    ps.GenNodePaths(j,False,withkind=False)
    for p in ps.paths:
        print p
    d = json.loads(j)
    ps.GenNodePaths(d,False,withkind=True)
    for p in ps.paths:
        print p
    pk = ps.GetPathKind(j)
    print pk
    print isCustomedKind('kik1k19')
