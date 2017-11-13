# -*- coding: utf-8 -*-
# author:BerryHN

# encoding:utf-8
import base64
import urllib
import urllib2
import json

from get_token import access_token
'''
图像审核接口
'''

request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/user_defined"

# 二进制方式打开图片文件
test=['cao.jpg','a.jpg']


f = open('/Users/zhiren1111/Desktop/test6.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
params = urllib.urlencode(params)

access_token = '24.7a04e909db281a876a6f520fcaca5433.2592000.1513146866.282335-10355547'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
target=-1
if content:
    print content
    result=json.loads(content)
    print result['conclusion']
    print result['data']
    for i in range(len(result['data'])):
        if result['data'][i]['type']==1:
            target=1
            continue

print(target)
