import requests
import tushare as ts
import json
import numpy as np
import pandas as pd



tushare = ts.get_hist_data(code='000001',start='2017-01-13',end='2017-01-18')
jsonStr = tushare.to_json(orient='columns')
# print(jsonStr)
data = json.loads(jsonStr)
open = list(data["date"].values())
open.sort()
print(open)
print(type(open))
print(open)

url = 'http://172.18.44.123:8004/history/getbar'
values = {"codes": ["000001.SZ"], "dateB": "2017-01-13", "dateE": "2017-01-18", "type": "normal", "fields": ["open", "close"]}
headers = {"Content-type": "application/json"}
s = requests.Session()

s.headers.update(headers)
r = s.post(url, json=values).text
# print(r)
# print(type(r))
json_test = json.loads(r)
# print(type(json_test))
data_test = json_test["datas"]
field = json_test["fields"]
open_index = field.index("open")
open_test = data_test[open_index]
open_test.sort()
# print(open_test)