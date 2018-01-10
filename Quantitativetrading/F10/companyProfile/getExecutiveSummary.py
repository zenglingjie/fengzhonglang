#高管简介
import requests
import pandas as pd
import pyodbc

#接口请求
content = {'secuCode':'000001'}
response = requests.get(url='http://172.18.44.120:8050/company-event/stocksData/companyProfile/getExecutiveSummary',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
dict = value_[2]
print(dict)

#数据库请求
data = open('F:/Quantitativetrading/F10/sql/getExecutiveSummarySQL.txt', 'r+')
TGWConnStr = ('Driver={MySQL ODBC 5.3 Unicode Driver};'
            'Server=%s;Port=%s;'
            'Database=%s;User=%s;'
            ' Password=%s;Option=3;'
            % ('172.18.44.5', '3306', 'jydb', 'jydb', '123456'))
req = pyodbc.connect(TGWConnStr)
df = pd.read_sql(data.read(),req)
dictionary = df.to_dict(orient='dict')
print(dictionary)
