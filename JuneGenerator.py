#-*- encoding: utf-8 -*-
'''
Created on 2013-12-11

@author: joel
'''
import datetime
import random
import string
import time
import uuid
from JuneGenEnName import gen_one_or_two_words
from JuneChinese import RandomChar
from JuneIdCardNo import _getCardNo,getdate,_city_code_dict
def telephone_head3_range():
    #yidong
    list = [x for x in range(134,139)]
    list.extend([x for x in range(150,152)])
    list.extend([x for x in range(157,159)])
    list.extend([x for x in range(181,183)])
    list.extend([x for x in range(187,188)])
    list.append(147)
    #dianxin
    list.append(133)
    list.append(153)
    list.append(180)
    list.append(189)
    #liantong
    list.extend([x for x in range(130,132)])
    list.extend([x for x in range(155,156)])
    list.extend([x for x in range(185,186)])
    numArray = []
    for i in range(len(list)):
        numArray.append(str(list[i]))
    return numArray

def mk_telephone_prefix():
    return string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],3)).replace(' ','')+'-'+\
            string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],8)).replace(' ','')+\
            string.join(random.sample(['-','#'],1)).replace(' ','')+\
            string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],random.randint(1,4))).replace(' ','')
def mk_telephone():
    return string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],3)).replace(' ','')+'-'+\
            string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],8)).replace(' ','')
def mk_moblie_prefix():
    return string.join(random.sample(['+86','17951','12593'],1)).replace(' ','') +\
            string.join(random.sample(telephone_head3_range(),1)).replace(' ','') +\
            string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],8)).replace(' ','')
def mk_moblie():
    return string.join(random.sample(telephone_head3_range(),1)).replace(' ','') +\
            string.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],8)).replace(' ','')
                        
def mk_phone():
    rd = random.randint(0,20)
    if(rd == 0):
        return mk_telephone()
    elif(rd == 1):
        return mk_telephone_prefix()
    elif(rd == 2):
        return mk_moblie()
    else:
        return mk_moblie_prefix()


#MCC = {"460":"CNY","520":"THB","452":"VND","724":"BRL","510":"IDR","502":"MYR","250":"RUB","404":"INR","655":"ZAR","602":"EGP","470":"BDT","716":"PES","621":"NGN","334":"MXN","410":"PRK","639":"KES","286":"TRY","432":"IRR","515":"PHP","415":"LBP","418":"IQD","620":"GHS","430":"SAR","525":"SGD","310":"USD"}
MCC = {"240":"EUR","248":"EUR","460":"CNY","520":"THB",\
             "452":"VND","724":"BRL","510":"IDR","502":"MYR",\
             "250":"RUB","404":"INR","655":"ZAR","602":"EGP",\
             "470":"BDT","716":"PES","621":"NGN","334":"MXN",\
             "410":"PRK","639":"KES","286":"TRY","432":"IRR",\
             "515":"PHP","415":"LBP","418":"IQD","620":"GHS",\
             "430":"SAR","525":"SGD","310":"USD"} 
def GetCurrency(st):
    try:
        Cu = MCC[st.strip()[:3]]
    except Exception,ex:
            raise Exception("Don't deploy correspondant currency")
    else:
        return Cu
    
def Getimsi():
#    return string.join(random.sample(['460','724','520','510',
#                  '621','466','250','452','515','502'],1)).replace(' ','')+\
#                  _RandomString('09',12)
    return string.join(random.sample(MCC.keys(),1)).replace(' ','')+\
              _RandomString('09',12) 
def Mk_imsi(n):
    if(n == 1):
        return Getimsi()+','+Getimsi()+','+Getimsi()
    elif(n == 2):
        return Getimsi()+','+Getimsi()+','+Getimsi()+','+Getimsi()
    elif(n == 3):
        return ""
    elif(n == 4):
        return " "
    else:
        return Getimsi()


def password():
    rd = random.randint(1,32)
    return RandomStringWithInt(rd)

def EnlargeRangebyMultiple(ls,num):
    return ls*num
def Randomint(rd):
    charArray = Alphets('09')
    quanta, leftover = divmod(rd,len(charArray))
    if(leftover != 0):
        quanta += 1
    charArray = EnlargeRangebyMultiple(charArray,quanta)
    return string.join(random.sample(charArray,rd)).replace(' ','')
    
def RandomString(rd):
    charArray = Alphets('aZ')
    quanta, leftover = divmod(rd,len(charArray))
    if(leftover != 0):
        quanta += 1
    charArray = EnlargeRangebyMultiple(charArray,quanta)
    return string.join(random.sample(charArray,rd)).replace(' ','')
def RandomStringWithInt(rd):
    charArray = Alphets('aA0')
    quanta, leftover = divmod(rd,len(charArray))
    if(leftover != 0):
        quanta += 1
    charArray = EnlargeRangebyMultiple(charArray,quanta)
    return string.join(random.sample(charArray,rd)).replace(' ','')
    
def RandomStringWithIntS(rd):
    charArray = Alphets('read')
    quanta, leftover = divmod(rd,len(charArray))
    if(leftover != 0):
        quanta += 1
    charArray = EnlargeRangebyMultiple(charArray,quanta)
    return string.join(random.sample(charArray,rd)).replace(' ','')
def RandomStringWithIntSX(rd):
    charArray = Alphets('noread')
    quanta, leftover = divmod(rd,len(charArray))
    if(leftover != 0):
        quanta += 1
    charArray = EnlargeRangebyMultiple(charArray,quanta)
    return string.join(random.sample(charArray,rd)).replace(' ','')

def _RandomString(kind,rd):
    charArray = Alphets(kind)
    quanta, leftover = divmod(rd,len(charArray))
    if(leftover != 0):
        quanta += 1
    charArray = EnlargeRangebyMultiple(charArray,quanta)
    return string.join(random.sample(charArray,rd)).replace(' ','')  

def RandomUrl():
    return 'http://www.' + string.join(random.sample(['baidu','QQ','xinlang','sky-mobi',\
                                                  'youtube','twitter','facebook','msn',
                                                  'renren'],1)).replace(' ','') +\
                                                  string.join(random.sample(['.com','.cn'],1)).replace(' ','')


def genuuid(kind='string'):
    if kind == 'string':
        return uuid.uuid4()
    else:
        return uuid.uuid1()
def gen_day(jmonth):
    jmonth = int(jmonth)
    if jmonth in (1,3,5,7,8,10,12):
        return  random.randint(1,31)
    elif jmonth in (4,6,9,11):
        return random.randint(1,30)
    elif jmonth == 2:
        return random.randint(1,28)
    else:
        print(('genday-None:',jmonth,type(jmonth)))
        
        return random.randint(1,28)
def gen_max_day(jmonth):
    jmonth = int(jmonth)
    if jmonth in (1,3,5,7,8,10,12):
        return  31
    elif jmonth in (4,6,9,11):
        return 30
    elif jmonth == 2:
        return 28
    else:
        print(('genday-None:',jmonth,type(jmonth)))
        return 27
def isCorrectday(m,d):
    m = int(m)
    d = int(d)
    if m in (1,3,5,7,8,10,12):
        if d <= 31:
            return True
        else:
            return False
    elif m in (4,6,9,11):
        if d <= 30:
            return True
        else:
            return False
    elif m == 2:
        if d < 29:
            return True
        else:
            return False
    return False

def mk_datetime_specified(Itimetuple,isstamptime=False):
    if Itimetuple[4:6] == '00':
        Itimetuple = Itimetuple[:5]+'1'+Itimetuple[6:]
    if Itimetuple[6:8] == '00':
        Itimetuple = Itimetuple[:7]+'1'+Itimetuple[8:]
    y,m,d,h,jmin,s,ms= Itimetuple[0:4],Itimetuple[4:6],Itimetuple[6:8],Itimetuple[8:10],Itimetuple[10:12],Itimetuple[12:14],Itimetuple[14:16]
    print y,m,d,h,jmin,s,ms
    Rtime = datetime.datetime(int(y),int(m),int(d),int(h),int(jmin),int(s),int(ms))
    if isstamptime == False:
        return Rtime
    else:
        return time.mktime(Rtime.timetuple()) 

def get_now_str_time():
    t = time.localtime()
    return str(t.tm_year).rjust(2,'0')+str(t.tm_mon).rjust(2,'0')+str(t.tm_mday).rjust(2,'0')+str(t.tm_hour).rjust(2,'0')+str(t.tm_min).rjust(2,'0')+str(t.tm_sec).rjust(2,'0')
def range_date(datestartstring,datestopstring):
    if len(datestopstring) == 4:
        datestopstring += '12'#month
    if len(datestopstring) == 6:
        datestopstring += str(gen_max_day(datestopstring[4:6]))#day
    if len(datestopstring) == 8:
        datestopstring += '23'#hour
    if len(datestopstring) == 10:
        datestopstring += '59'#min
    datestartstring = datestartstring.ljust(16,'0')
    datestopstring = datestopstring.ljust(16,'0')
    if datestartstring[4:6] == '00':
        datestartstring = datestartstring[:5]+'1'+datestartstring[6:]
    if datestartstring[6:8] == '00':
        datestartstring = datestartstring[:7]+'1'+datestartstring[8:] 
    if long(datestartstring) > long(datestopstring):
        return False
    ystart,ystop,mstart,mstop,dstart,dstop,hstart,hstop,minstart,minstop = \
       int(datestartstring[0:4]),int(datestopstring[0:4]),int(datestartstring[4:6]),int(datestopstring[4:6]),\
       int(datestartstring[6:8]),int(datestopstring[6:8]),int(datestartstring[8:10]),int(datestopstring[8:10]),\
       int(datestartstring[10:12]),int(datestopstring[10:12])
    ############jyear####################
    jyear = random.randint(ystart,ystop)
    ############jmonth####################
    if ystart < jyear and jyear < ystop:
        jmonth = random.randint(1,12)
        jday = int(gen_day(jmonth))
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    elif jyear == ystart and jyear != ystop:
        jmonth = random.randint(mstart,12)
        jday = int(gen_day(jmonth))
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    elif jyear == ystop and jyear !=ystart:
        jmonth = random.randint(1,mstop)
        jday = int(gen_day(jmonth))
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    else:#ystart == ystop
        jmonth = random.randint(mstart,mstop)
        jday = int(gen_day(jmonth))
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    ############jday####################
    if mstart < jmonth and jmonth !=mstop:
        jday = int(gen_day(jmonth))
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    elif jmonth == mstart and jmonth != mstop:
        tday = random.randint(dstart,31)
        while not isCorrectday(jmonth,tday):
            tday -= 1
            if tday > 0:
                tday = random.randint(1,27)
                break
        jday =  tday
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    elif jmonth == mstop and jmonth !=mstart:
        tday = random.randint(1,dstop)
        while not isCorrectday(jmonth,tday):
            tday -= 1
            if tday > 0:
                tday = random.randint(1,27)
                break
        jday =  tday
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    else:
        tday = random.randint(dstart,dstop)
        while not isCorrectday(jmonth,tday):
            tday -= 1
            if tday > 0:
                tday = random.randint(1,27)
                break
        jday =  tday
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    ############jhour####################  
    if  dstart < jday and jday < dstop:
        jhour = random.randint(0,23)
        jmin = random.randint(0,59)
    elif jday == dstart and jday != dstop:
        jhour = random.randint(hstart,23)
        jmin = random.randint(0,59)
    elif jday == hstop and jday != hstart:
        jhour = random.randint(0,hstop)
        jmin = random.randint(0,59)
    else:
        jhour = random.randint(hstart,hstop)
        jmin = random.randint(0,59)
    ############jmin####################  
    if hstart < jhour and jhour < hstop:
        jmin = random.randint(0,59)
    elif jhour == hstart and jhour != hstop:
        jmin = random.randint(minstart,59)
    elif jhour == hstop and jhour != hstart:
        jmin = random.randint(0,minstop)
    else:
        jmin = random.randint(minstart,minstop)
   
    return str(jyear).rjust(2,'0')+str(jmonth).rjust(2,'0')+str(jday).rjust(2,'0')+str(jhour).rjust(2,'0')+str(jmin).rjust(2,'0')+\
        str(random.randint(1,59)).rjust(2,'0')+str(random.randint(1,100)).rjust(3,'0')
def Alphets(kind):
    ls = []
    if(kind == 'az'):#a-z
        for i in range(65,90):
            ls.append(chr(i))
    elif(kind == 'AZ'):#A-Z
        for i in range(97,122):
            ls.append(chr(i))
    elif(kind == 'aZ'):#a-z  #A-Z
        for i in range(65,90):
            ls.append(chr(i))
        for i in range(97,122):
            ls.append(chr(i))
    elif(kind == '09'):#0-9
        for i in range(48,57):
            ls.append(chr(i))
    elif(kind == 'a0'):#a-z #0-9
        for i in range(65,90):
            ls.append(chr(i))
        for i in range(48,57):
            ls.append(chr(i))
    elif(kind == 'A0'):#A-Z #0-9
        for i in range(97,122):
            ls.append(chr(i))
        for i in range(48,57):
            ls.append(chr(i))
    elif(kind == 'aA0'):#a-z #A-Z #0-9
        for i in range(65,90):
            ls.append(chr(i))
        for i in range(97,122):
            ls.append(chr(i))
        for i in range(48,57):
            ls.append(chr(i))
    elif(kind == '#*'):#~!@#$%^&*()_+-=
        for i in range(32,47):
            ls.append(chr(i))
        for i in range(58,64):
            ls.append(chr(i))
        for i in range(91,96):
            ls.append(chr(i))
        for i in range(123,126):
            ls.append(chr(i))
    elif(kind == 'read'):#be able to recognized or read by people
        for i in range(32,126):
            ls.append(chr(i))
    elif(kind == 'noread'):#be not able to recognized or read by people
        for i in range(0,31):
            ls.append(chr(i))
        ls.append(chr(127))
    elif(kind == 'ascii'): #all charaters in ASCII table
        for i in range(0,127):
            ls.append(chr(i))
    elif(kind == 'X'):#all charaters not in ASCII table but with 8bits in width 
        for i in range(128,256):
            ls.append(chr(i))
    elif(kind == 'all'):#all charaters with 8bits in width
        for i in range(0,256):
            ls.append(chr(i))
    elif(kind == '16'):#all charaters with 8bits in width
        for i in range(0,9):
            ls.append(chr(i))
        for i in range(97,102):
            ls.append(chr(i))
    else:
        print('No match kind')
        return None
    return ls
def mkIp():
    return str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))
def mkEmail():
    return RandomStringWithInt(random.randint(6,32))+string.join(random.sample(['@126.com','@gmail.com','@qq.com','@163.com',\
                                                  '@topchinacredit.com','@deppon.com','@hotmail.com','@yeah.com',
                                                  '@facebook.com','@twitter.com','@youtube.com'],1)).replace(' ','')
def mkName():
    rd = random.randint(0,1)
    if rd == 1:
        return RandomChar().Utf8()+RandomChar().Utf8()
    else:
        return gen_one_or_two_words()
    return
def mkChinese(length):
    cs =''
    for i in xrange(length):
        cs += RandomChar().Utf8()
    return cs
def mkCity():
    province = ('北京市（京', 
                '天津市（津',
                '上海市（沪）',
                '重庆市（渝）' ,
                '河北省（冀）' ,
                '河南省（豫）' ,
                '云南省（云）' ,
                '辽宁省（辽）' ,
                '黑龙江省（黑）' ,
                '湖南省（湘）' ,
                '安徽省（皖）' ,
                '山东省（鲁）' ,
                '新疆维吾尔（新）' ,
                '江苏省（苏）' ,
                '浙江省（浙）' ,
                '江西省（赣）' ,
                '湖北省（鄂）' ,
                '广西壮族（桂）', 
                '甘肃省（甘）' ,
                '山西省（晋）' ,
                '内蒙古（蒙）' ,
                '陕西省（陕）' ,
                '吉林省（吉）' ,
                '福建省（闽）' ,
                '贵州省（贵） ',
                '广东省（粤）' ,
                '青海省（青）' ,
                '西藏（藏）' ,
                '四川省（川）' ,
                '宁夏回族（宁）' ,
                '海南省（琼）',
                '台湾省（台）',
                '香港特别行政区',
                '澳门特别行政区')
    return province[random.randint(0,len(province)-1)]
def mkMac():
    mac_bin_list = []
    mac_hex_list = []
    for i in range(1,7):
        i = random.randint(0x00,0xff)
        mac_bin_list.append(i)
    for j in mac_bin_list:
        mac_hex_list.append(hex(j))
    Hardware = ":".join(mac_hex_list).replace("0x","")
    return Hardware
def mkID(num):
    sex = str(random.randint(1,2))
    yyyymmdd = getdate(limit_bottom='1916', limit_top='2016')
    return _getCardNo('110100', yyyymmdd, sex, num)
    
if __name__ == '__main__':
    print mkChinese(10)
    print mkMac()
    t = '123456789'
    print t[0:4],t[4:5]
    print mkName()
    for i in xrange(10):
        print mkCity()
    print mkID(10)
    print _city_code_dict()