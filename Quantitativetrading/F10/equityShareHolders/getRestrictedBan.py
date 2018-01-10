#受限解禁
import requests
import pyodbc
import pandas as pd

#接口请求
content = {'secuCode':'000001'}
response = requests.get(url='http://172.18.44.120:8050/equity-share-holders/stocksData/equityShareHolders/getRestrictedBan',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
print(value_)

#数据库请求
data = open('F:/Quantitativetrading/F10/sql/getRestrictedBanSQL.txt', 'r+')
TGWConnStr = ('Driver={MySQL ODBC 5.3 Unicode Driver};'
            'Server=%s;Port=%s;'
            'Database=%s;User=%s;'
            ' Password=%s;Option=3;'
            % ('172.18.44.5', '3306', 'jydb', 'jydb', '123456'))
req = pyodbc.connect(TGWConnStr)
df = pd.read_sql(data.read(),req)
dictionary = df.to_dict(orient='dict')
DBvalue = {}
for i in dictionary.keys():
    values = dictionary.get(i)
    DBvalue[i] = values.pop(0)
print(DBvalue)
