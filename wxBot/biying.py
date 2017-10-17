#!/usr/bin/env python3
# -*- coding: utf-8
#http://cn.bing.com/az/hprichbg/rb/CoastalBeech_ZH-CN8739604309_1920x1080.jpg
#http://cn.bing.com/az/hprichbg/rb/LittleAuks_ZH-CN9796184036_1920x1080.jpg
import re
import urllib.request
import bs4
import sys
import json
import csv
import biYingInfo
count1=0

html1 = urllib.request.urlopen("http://cn.bing.com/").read()  # 打开url读取
#print(html1)
html1 = str(html1)  # 因为是bytes-like数据，需要转化
pat1 = '(url:.{10,90}jpg)'  # 匹配开头和结尾，找网页中出现一次的字符串作为标识   文/时尚旅游
pat2 = 'hplaSnippet(.*?)文/时尚旅游'
result1 = re.compile(pat1).findall(html1)[0]  # 编译正则表达式，findall 找到所有符合正则的列表
#result2 = re.compile(pat2).findall(html1)
#print(result2)

list1=result1.split('\"')
str1=list1[1]
str1="http://cn.bing.com"+str1
#print(str1)

u=urllib.request.urlopen(str1)
data=u.read()
with open("biying.jpg",'wb') as f:
    f.write(data)
biYingInfo.getPicInfo()
print("finished")

