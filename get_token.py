# -*- coding: utf-8 -*-
# author:BerryHN

# -*- coding: utf-8 -*-
# author:BerryHN
import urllib, urllib2, sys
import ssl
import json

def Get_token(ak,sk):
    try:
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+ak+'&client_secret='+sk
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        content = response.read()
        if (content):
            result = eval(content)
            token=result['access_token']
    except:
        token=''


    return token





# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MuxDqUOMNloGEsmzZGE7Gi4V&client_secret=f2NUjf4qdRu1O87YDCRGUaWczVaNf5lH'

request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
#if (content):
    #print(content)

#result=eval(content)
#print result["access_token"]
ak='MuxDqUOMNloGEsmzZGE7Gi4V'
sk='f2NUjf4qdRu1O87YDCRGUaWczVaNf5lH'
access_token=Get_token(ak,sk)

