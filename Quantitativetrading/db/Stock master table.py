import requests
import tushare as ts
import json


tushare =ts.get_stock_basics()
# print(tushare)
jsonStr = tushare.to_json(orient='columns')
# print(jsonStr)
jsonStr1 = tushare.to_json(orient='records')
# print(jsonStr1)
jsonStr2 = tushare.to_json(orient='index')
# print(jsonStr2)
jsonStr3 = tushare.to_json(orient='split')
# print(jsonStr3)
jsonStr4 = tushare.to_json(orient='values')
# print(jsonStr4)

code_ = json.loads(jsonStr3)
code_ = list(code_["index"])
code_.sort()
print(code_)
print(len(code_))


url = 'http://172.18.44.123:8004/main/getsecu'
values = {}
headers = {"Content-type": "application/json"}
s = requests.Session()
s.headers.update(headers)
r = s.post(url,json=values).text
json_test = json.loads(r)

a =[]
for code in json_test['datas']:
    a.append(code['code'][0:6])
print(len(a))
print(set(code_) ^ set(a))