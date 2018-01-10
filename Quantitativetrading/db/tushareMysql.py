import pyodbc
import tushare as ts
import requests
import json

tushare = ts.get_suspended()
print(tushare)

# TGWConnStr = (
#         'Driver={MySQL ODBC 5.1 Driver};Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
#         % ('172.18.44.122', '3306', 'management', 'testuser', 'test@tgw88'))
# req = pyodbc.connect(TGWConnStr)
# cur = req.cursor()
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

url = 'http://172.18.44.123:8004/v/suspended'

values = {"codes":["000669.SZ","601388.SH"],"dateB":"2017-05-04","dateE":"2017-05-05"}

headers = {"Content-type": "application/json"}
s = requests.Session()
s.headers.update(headers)
r = s.post(url, json=values).text
json_test = json.loads(r)
# print(json_test)

date =[]
for code in json_test['datas']:
    date.append(code['code'][0:6])

print(date)
print(len(date))
