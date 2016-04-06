#效仿json框架数据生成器                                                                                                                                        

##使用方法: 
```
j = '{"name":"knk0k0","soItemDtoList": [{"ip":"kipk0k0","productId": ["kidk1k19",{"email":"kemailk0k0","a":[{"aa":"june"},2,3]}]}, {"count": "kik2k3"}],"ddd">
_dict = ImitateJson(json.loads(j))
print json.dumps(_dict)
print IsSameByKey(j, json.dumps(_dict))
_dict = ImitateJson(json.loads(j),10)
for d in _dict:
    print IsSameByKey(j, json.dumps(d)),d
//////////////////////print///////////////////
{"boolv": true, "name": "\u7c72\u58f5", "nullv": null, "soItemDtoList": [{"ip": "222.106.30.227", "productId": ["110100195508032809", {"a": [{"aa": "FdrIbo"}>
True
True {'boolv': True, 'name': 'Wilson Conrad', 'nullv': None, 'soItemDtoList': [{'ip': '27.48.208.46', 'productId': ['110100200401166624', {'a': [{'aa': 'MYU1>
True {'boolv': False, 'name': '\xe6\x8d\x9a\xe6\xb3\x87', 'nullv': None, 'soItemDtoList': [{'ip': '248.249.59.17', 'productId': ['110100195610237421', {'a': >
True {'boolv': False, 'name': '\xe9\x8e\xba\xe5\xab\xb0', 'nullv': None, 'soItemDtoList': [{'ip': '33.154.77.20', 'productId': ['110100196505068288', {'a': [>
True {'boolv': False, 'name': '\xe6\xb2\x9a\xe6\xb0\xb7', 'nullv': None, 'soItemDtoList': [{'ip': '162.186.47.65', 'productId': ['110100198207196029', {'a': >
True {'boolv': True, 'name': '\xe6\xb8\xb3\xe6\x84\x92', 'nullv': None, 'soItemDtoList': [{'ip': '184.199.60.92', 'productId': ['110100197603034545', {'a': [>
True {'boolv': False, 'name': '\xe8\x9f\xbc\xe6\x93\xa9', 'nullv': None, 'soItemDtoList': [{'ip': '232.189.119.211', 'productId': ['110100195402062348', {'a'>
True {'boolv': True, 'name': 'Sammy', 'nullv': None, 'soItemDtoList': [{'ip': '72.146.84.95', 'productId': ['110100191812146909', {'a': [{'aa': 'gWkS'}, 267,>
True {'boolv': False, 'name': '\xe5\x9b\xbe\xe5\x9e\x8d', 'nullv': None, 'soItemDtoList': [{'ip': '99.110.138.60', 'productId': ['11010019780211736X', {'a': >
True {'boolv': False, 'name': 'Braydon Shauna', 'nullv': None, 'soItemDtoList': [{'ip': '183.92.85.211', 'productId': ['110100197301033344', {'a': [{'aa': 'T>
True {'boolv': True, 'name': 'Megan Tricia', 'nullv': None, 'soItemDtoList': [{'ip': '31.9.103.29', 'productId': ['110100192407057069', {'a': [{'aa': 'YI'}, >

```
