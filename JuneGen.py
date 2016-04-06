#coding=utf-8
'''
Created on 2016年4月1日

@author: duqiong
'''
from JuneGenData import genDataByRulesPath
from JuneParserJson import ParserJson
from JuneRules import genDataAccordingRules

def ImitateJson(dictOjson,num=1):
    '''
    在python眼里dict与jsonstr通过json模块可以互转
    '''
    ps = ParserJson()
    pathKind = ps.GetPathKind(j)#获取路径与类型框架path/kind(dict)
    if num>1:
        rlist = []
        for i in xrange(num):
            pathData = genDataAccordingRules(pathKind)#根据类型框架生成path/value(dict)
            rlist.append(genDataByRulesPath(pathData))#根据路径框架生成key/value(dict)
        return rlist
    else:
        pathData = genDataAccordingRules(pathKind)#根据类型框架生成path/value(dict)
        return genDataByRulesPath(pathData)#根据路径框架生成key/value(dict)

def ImitateJsonWithPK(pathKind):
    '''
    pathKind  must be the type of dict or json
    '''
    pathData = genDataAccordingRules(pathKind)#根据类型框架生成path/value(dict)
    rdict = genDataByRulesPath(pathData)#根据路径框架生成key/value(dict)
    return rdict

def IsSameByKey(json1,json2,compareWithKind=False):
    '''
    对比两个json串是否相似,不对比value
    compareWithKind：对比时，是否对比value的类型
    
    '''
    ps = ParserJson()
    if compareWithKind:
        pathrule1 = ps.GenNodePaths(json1)
        pathrule2 = ps.GenNodePaths(json2)
#         print pathrule1 ,pathrule2
        for p in pathrule1:
            if p not in pathrule2:
                return False
    else:
        pathkind1 = ps.GetPathKind(json1)
        pathkind2 = ps.GetPathKind(json2)
#         print pathkind1,pathkind2
        for p in pathkind1.keys():
            if p not in pathkind2.keys():
                return False
    return True
if __name__ =='__main__':
    import json
    j = '{"createtime":"idtrange(201603,20160306)","price":"irange(98,100)","status":"slist(pending,running)","name":"knk0k0","soItemDtoList": [{"ip":"kipk0k0","productId": ["kidk1k19",{"email":"kemailk0k0","a":[{"aa":"june"},2,"srange(10,15)"]}]}, {"count": "kik2k3"},"sdtrange(201601,20160202)","idtrange(201601,20160202)"],"ddd":123,"dfd":"ddf","boolv":true,"nullv":null}'
    _dict = ImitateJson(json.loads(j))
    print _dict
    print json.dumps(_dict)
    print IsSameByKey(j, json.dumps(_dict))
#     _dict = ImitateJson(json.loads(j),10)
#     for d in _dict:
#         print IsSameByKey(j, json.dumps(d)),d
