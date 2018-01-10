import requests
import tushare as ts
import json


tushare = ts.get_st_classified()
print(tushare)



url = 'http://localhost:8004/v/ST'#取ST
values = {"dateB":"1990-01-01","dateE":"2017-08-15"}
headers = {"Content-type": "application/json"}
s = requests.Session()
s.headers.update(headers)
r = s.post(url,json=values).text
json_test = json.loads(r)