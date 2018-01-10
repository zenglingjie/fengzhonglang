#历年分红融资
import requests
import pandas as pd
import pyodbc

#接口请求
content = {'secuCode':'000001', 'beginIndex': 0, 'recordNum': 10}
response = requests.get(url='http://172.18.44.120:8050/financing-share-bonus/stocksData/financingShareBonus/getDividendFinancingHis',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
del dict['id']
del dict['updatetime']
del dict['dividendimplementDate']
print(dict)



#数据库请求
data = open('F:/Quantitativetrading/F10/sql/getDividendFinancingHisSQL.txt', 'r+',encoding='utf-8')
TGWConnStr = ('Driver={MySQL ODBC 5.3 Unicode Driver};'
            'Server=%s;Port=%s;'
            'Database=%s;User=%s;'
            ' Password=%s;Option=3;'
            % ('172.18.44.5', '3306', 'jydb', 'jydb', '123456'))
req = pyodbc.connect(TGWConnStr)
df = pd.read_sql(data.read(),req)
dictionary = df.to_dict(orient='dict')
del dictionary['UpdateTime']
del dictionary['DividendImplementDate']
# print(dictionary)
DBvalue = {}
for i in dictionary.keys():
    values = dictionary.get(i)
    DBvalue[i] = values.pop(0)
print(DBvalue)


for key,values in DBvalue.items():
    v_dict = dict.get(key.lower())
    try:
        if abs(v_dict-values) >= 0.1:
            print(key, 'data not correct')
        elif v_dict and values is None:
            print(key,'is null')
    except Exception as e:
        print(key, 'not found')