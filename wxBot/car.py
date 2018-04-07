import urllib, urllib.request, sys
import base64
import ssl
#
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=de12ee225ed945bdb7c8a0eb2f633757&client_secret=4d126c36666446f1a4159d9469bac9b7'
# request = urllib.request.Request(host)
# request.add_header('Content-Type', 'application/json; charset=UTF-8')
# response = urllib.request.urlopen(request)
# content = response.read()
# if (content):
#     print(content)
#
#     '''7257256990b142d798539fcfa4a39027
# 4d126c36666446f1a4159d9469bac9b7'''
import urllib3,base64
from urllib.parse import urlencode
import json
import urllib3
http=urllib3.PoolManager()
request=http.request('GET',
                        'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vrUQ0HGh2onn5SwOs6KsXIUT&client_secret=m6zySPKC7WWYGYRcOy6W0KRIwuAPGikQ'
                    )

# print(request.data)

print(json.loads(request.data)['access_token'])


access_token=json.loads(request.data)['access_token']
http=urllib3.PoolManager()
url='https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+access_token
f = open('C:\\Users\\Administrator\\Desktop\\AAA.jpg','rb')
#参数image：图像base64编码
img = base64.b64encode(f.read())
params={'image':img}
#对base64数据进行urlencode处理
params=urlencode(params)
request=http.request('POST',
                      url,
                      body=params,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)





host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vrUQ0HGh2onn5SwOs6KsXIUT&client_secret=m6zySPKC7WWYGYRcOy6W0KRIwuAPGikQ'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
urllib3.disable_warnings()
access_token='24.63dc62e7c4f9efb5722aa068bd1219b4.2592000.1523882258.282335-10934719'##json.loads(content)['access_token']
http=urllib3.PoolManager()
url='https://aip.baidubce.com/rest/2.0/image-classify/v1/car?access_token='+access_token
f = open('C:\\Users\\Administrator\\Desktop\\AAA.jpg','rb')
#参数image：图像base64编码
img = base64.b64encode(f.read())
params={'image':img}
#对base64数据进行urlencode处理
params=urlencode(params)

request=http.request('POST',
                      url,
                      body=params,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)
d = json.loads(result)
print(d)

