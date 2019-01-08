#coding:utf-8
import requests

url = 'https://www.highpin.cn'
req = requests.get(url)
print(req.status_code)

