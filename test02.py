#coding:utf-8

import requests

url = 'http://www.baidu.com'
req = requests.get(url)
print(req.url,'\n',
      req.status_code,'\n',
      req.headers)