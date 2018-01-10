import requests
import tushare as ts
import json


tushare =ts.get_industry_classified()
# print(tushare)
# jsonStr = tushare.to_json(orient='columns')
# # # print(jsonStr)
# jsonStr1 = tushare.to_json(orient='records')
# # print(jsonStr1)
# jsonStr2 = tushare.to_json(orient='index')
# # # print(jsonStr2)
# jsonStr3 = tushare.to_json(orient='split')
# # # print(jsonStr3)
# jsonStr4 = tushare.to_json(orient='values')
# # # print(jsonStr4)
#
# code_ = json.loads(jsonStr1)
# code_ = list(code_["code"])
# code_.sort()
# print(code_)
# print(len(code_))


url = 'http://172.18.44.123:8004/v/split'#取送股
url_ = 'http://172.18.44.123:8004/v/dividend'#取分红
values = {"codes":["000600.SZ","600036.SH"]}
headers = {"Content-type": "application/json"}
s = requests.Session()
s.headers.update(headers)
r = s.post(url_,json=values).text
json_test = json.loads(r)

print(json_test)