#-*- coding: UTF-8 -*-
'''
Created on 2015年4月16日

@author: joel
'''
import random
class RandomChar():
    """用于随机生成汉字"""
    @staticmethod
    def Unicode():
        val = random.randint(0x4E00, 0x9FBF)
        return unichr(val)
    @staticmethod
    def Utf8():
        val = random.randint(0x4E00, 0x9FBF)
        return unichr(val).encode('utf-8')   
    
    @staticmethod
    def GB2312():
        head = random.randint(0xB0, 0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = ( head << 8 ) | (body << 4) | tail
        str = "%x" % val
        return str.decode('hex').decode('gb2312')
if __name__ == '__main__': 
    for i in xrange(10000):
        print RandomChar().Utf8()