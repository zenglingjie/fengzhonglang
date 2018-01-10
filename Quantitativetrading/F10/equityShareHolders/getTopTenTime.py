#十大流通股东/十大股东 时间列表
import requests
import pandas as pd
import pyodbc

#接口请求
content = {'secuCode':'000001','infotypecode':1}
response = requests.get(url='http://172.18.44.120:8050/equity-share-holders/stocksData/equityShareHolders/getTopTenTime',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
print(dict)

