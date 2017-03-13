#coding=utf-8
'''
Created on 2016年4月1日

@author: duqiong
'''
from JuneGenData import genDataByRulesPath
from JuneParserJson import ParserJson
from JuneRules import genDataAccordingRules,valish

def ImitateJson(dictOjson,num=1):
    '''
    在python眼里dict与jsonstr通过json模块可以互转
    '''
    ps = ParserJson()
#     pathKind = ps.GetPathKind(j)#获取路径与类型框架path/kind(dict)
    pathKind = ps.preConvert(j)#获取路径与类型框架path/kind(dict)
    print pathKind
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

def IsSameByKey(json1,json2,compareWithKind=False,escape=False):
    '''
    对比两个json串是否相似,不对比value
    compareWithKind：对比时，是否对比value的类型
    
    '''
    ps = ParserJson()
    if compareWithKind:
        pathrule1 = ps.GenNodePaths(json1)
        pathrule2 = ps.GenNodePaths(json2)
        if escape:
            pathrule1 = [valish(p) for p in pathrule1]
            pathrule2 = [valish(p) for p in pathrule2]
    else:
        pathkind1 = ps.GetPathKind(json1)
        pathkind2 = ps.GetPathKind(json2)
#         print pathkind1,pathkind2
        if escape:
            pathrule1 = [valish(p) for p in pathkind1.keys()]
            pathrule2 = [valish(p) for p in pathkind2.keys()]
        else:
            pathrule1 = pathkind1.keys()
            pathrule2 = pathkind2.keys()
    for p in pathrule1:
        if p not in pathrule2:
            return False
    return True
