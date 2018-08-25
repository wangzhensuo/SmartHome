# -*- coding:utf-8 -*-
import urllib.request
import json
import time
import datetime
import random
import requests

APIKEY = 'fz6gLsGrLgQOUYJGHJKHKLJHJHL='  # 改成你的APIKEY
apiurl = 'http://api.heclouds.com/devices/123456789/datapoints' #链接里面的数字要改成自己的
apiheaders = {'api-key': APIKEY, 'Content-Length': '120'}
def get_temp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close()
    # 向控制台打印结果
    print("CPU的温度值为: %.3f" % temp)
    # 返回温度值
    return temp


def http_put():
    # temperature = get_temp()  # 获取CPU温度并上传
    temperature = random.randint(60,100)
    CurTime = datetime.datetime.now()
    payload = {'datastreams': [{"id": "girlA", "datapoints": [{"at": CurTime.isoformat(), "value": temperature}]}]}
    # payload = {"datastreams": [{"id": "girlA", "datapoints": [{"value": 11}]}]}
    print("当前时间为： %s" % CurTime.isoformat())
    print("上传值为: %.3f" % temperature)

    jdata = json.dumps(payload)  # 对数据进行JSON格式化编码
    # 打印json内容
    print(jdata)
    r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))
    return r

while True:
    time.sleep(2)
    resp = http_put()
    print("OneNET请求结果:\n %s" % resp)
