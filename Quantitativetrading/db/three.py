import requests
import tushare as ts
import json
import operator


df = ts.get_hist_data(code='000001',start='2016-01-13',end='2017-06-18')
jsonStr1 = df.to_json(orient='records')
jsonStr2 = df.to_json(orient='index')
jsonStr3 = df.to_json(orient='split')
jsonStr4 = df.to_json(orient='values')
jsonStr = df.to_json(orient='columns')

data = json.loads(jsonStr3)
date = list(data["index"])
date.sort()
print(date)
print(len(date))

open = json.loads(jsonStr)
open = list(open['open'].values())
open.sort()
# print(open)


url = 'http://172.18.44.123:8004/history/getbar'

values = {"codes": ["000001.SZ"], "dateB": "2016-01-13", "dateE": "2017-06-18", "type": "normal", "fields": ["open", "close"]}

headers = {"Content-type": "application/json"}
s = requests.Session()

s.headers.update(headers)
r = s.post(url, json=values).text
json_test = json.loads(r)
date_test = json_test["dates"]
print(date_test)
print(len(date_test))

code_test = json_test["datas"]
field = json_test["fields"]
open_index = field.index("open")
open_test = code_test[open_index]
open_test.sort()
# print(open_test)


print(set(date_test) ^ set(date))
print(set(open_test) ^ set(open))