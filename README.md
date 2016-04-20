# 数据银行 #
>
> ***背景***
>>
>>  1. 自动化时需要测试数据，我们使用excel表手工来维护测试数据
>>  2. 多项目要使用多excel表来维护各自测试数据。
>>  3. 测试时每次使用数据时都是一样的,在用户注册，进件等场景不能再使用。
>>  4. 在mock api接口时，模拟的数据不够真实。
>>
>
> ***目的***
>>
>>  1. 一个服务器来维护多个项目的测试数据;
>>  2. 提供api接口提供数据(json格式)，方便自动化,mock 项目api接口时使用;
>>  3. 数据可以根据"规则"制定符合业务的数据;
>>  4. 每次使用的数据不一样,在用户注册，进件等场景不再考虑数据不可用情况。
>>  5. 提供web端(后期做)。
>>
>

>
> ***解决方案***
>
>  解决方案：测试团队自己开发。
>>  具体实现如下：
>>
>>  设计：
>>  1. 输入规则->生成数据规则并入库(供下次通过编号使用数据)->数据生成器->输出定制的数据
>>  2. 输入编号->数据生成器->输出定制的数据
>>  
>>  规则如下:
>>
```
基本类型:t-电话号码,n-名字(有中文与英文),id-uuid,mac-MAC地址,ip-IP,email-邮件,is-数字与字符混和的字符串,i-int类型,s-只有字符的字符串,chinses-汉,city-城市名,还有后期补充
语法k类型k上限k下限
```
```
高级类型:slist－string的列表,ilist－int的列表,irange－int的范围,srange－string的范围,idtrange－int date的范围,sdtrange－string date的范围,dttrange－datetime的范围,dtrange－date的范围
```
>>
> 
>  ***用法***
>>  curl -d '{"name":"joel","lat":"123","lng":"145","money":28}' http://服务器ip:port/getdata?count=5
```会批量模仿输出5个测试数据,注意没有使用任何规则,输出只是原始数据自我模仿
{"lat": "6eFEJ", "money": 939, "lng": "Avem", "name": "Uv"}
{"lat": "FKVg", "money": 761, "lng": "7", "name": "mucL"}
{"lat": "eRj", "money": 876, "lng": "8pAOH", "name": "x4INR"}
{"lat": "fSFY", "money": 521, "lng": "u74EG", "name": "ixD"}
{"lat": "iuwKq", "money": 858, "lng": "sV", "name": "YicEj"}
```
>>
>>  curl -d '{"name":"knk0k0","lat":123,"lng":145,"islogin":true}' http://服务器ip:port/getdata?count=5
```会批量模仿输出5个定制数据
{"islogin": false, "lat": 833, "lng": 139, "name": "Carly Uriah"}
{"islogin": true, "lat": 164, "lng": 579, "name": "\u8b24\u853c"}
{"islogin": true, "lat": 19, "lng": 461, "name": "\u83aa\u7c82"}
{"islogin": false, "lat": 986, "lng": 481, "name": "Nieve Yehudi"}
{"islogin": false, "lat": 127, "lng": 553, "name": "Zylen"}
```
>>
>>  curl -d '{"ip":"kipk0k0","lat":"irange(100,105)","lng":"irange(20,100)","date":"idtrange(20160401,20160405)","createdate":"sdtrange(20150401,2016)"}' http://服务器ip:port/getdata?count=5
```会批量模仿输出5个定制数据
{"date": 20160405165457051, "ip": "141.92.73.223", "createdate": "20150818103847073", "lat": 102, "lng": 88}
{"date": 20160403033345098, "ip": "96.190.112.242", "createdate": "20151124180508098", "lat": 101, "lng": 40}
{"date": 20160404092937011, "ip": "55.102.67.168", "createdate": "20150605200225070", "lat": 101, "lng": 62}
{"date": 20160405062012074, "ip": "164.98.119.96", "createdate": "20161220193522014", "lat": 105, "lng": 61}
{"date": 20160402164601022, "ip": "119.45.93.68", "createdate": "20160803170613032", "lat": 100, "lng": 47}
```
>>
>>  curl -d '{"age@":27,"email":"kemailk0k0","city":"kcityk0k0","password":"kisk12k32"}' http://服务器ip:port/getdata?count=5
```会批量模仿输出5个定制数据,注意age是值是固定的
{"city": "\u6e56\u5317\u7701\uff08\u9102\uff09", "age": 27, "password": "WOt5c1pDvRdaQEPiCSg", "email": "D1PwWAg3q68myXMcukCVhLB@qq.com"}
{"city": "\u9655\u897f\u7701\uff08\u9655\uff09", "age": 27, "password": "tAU5JyjLCvr6uxHnX1VYmOPMeB2s", "email": "NTc2CQ5ndEsyuw0F@hotmail.com"}
{"city": "\u8fbd\u5b81\u7701\uff08\u8fbd\uff09", "age": 27, "password": "4yX6tMSONdo2r5JYQ3jUiV1gwDWfKn", "email": "U378ajKAwXkf52SCtQueHyG@gmail.com"}
{"city": "\u6e56\u5357\u7701\uff08\u6e58\uff09", "age": 27, "password": "7FLKGfiPgRuBExd3", "email": "jaTyI1rMmLSHlOsfxJk@gmail.com"}
{"city": "\u4e91\u5357\u7701\uff08\u4e91\uff09", "age": 27, "password": "kvaMqi8HxQ6Anwu", "email": "sb1TUl6C7RiLnhSEFjQVX2fto3@126.com"}
```
>>
>>  curl -d '{"@age":27,"email":"kemailk0k0","city":"kcityk0k0","password":"kisk12k32"}' http://服务器ip:port/getdata?count=5
```会批量模仿输出5个定制数据,但是自己的复制
{"city": "kcityk0k0", "age": 27, "password": "kisk12k32", "email": "kemailk0k0"}
{"city": "kcityk0k0", "age": 27, "password": "kisk12k32", "email": "kemailk0k0"}
{"city": "kcityk0k0", "age": 27, "password": "kisk12k32", "email": "kemailk0k0"}
{"city": "kcityk0k0", "age": 27, "password": "kisk12k32", "email": "kemailk0k0"}
{"city": "kcityk0k0", "age": 27, "password": "kisk12k32", "email": "kemailk0k0"}