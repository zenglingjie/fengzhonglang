#主要指标
import requests
import json
import pyodbc
import pandas as pd
import numpy as np


content = {'secuCode':600036, 'type': 0, 'beginIndex': 0, 'recordNum': 10}
response = requests.get(url='http://172.18.44.123:8002/stocksData/financialAnalysis/getMainIndicators',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
del dict['id']
del dict['updatetime']
del dict['secucode']
del dict['type']
del dict['time']
del dict['industrytype']
# print(type(dict))
print(dict)
print(len(dict.keys()))

data = open('F:/Quantitativetrading/F10/sql/getMainIndicatorsSQL.txt', 'r+')
TGWConnStr = ('Driver={MySQL ODBC 5.3 Unicode Driver};'
            'Server=%s;Port=%s;'
            'Database=%s;User=%s;'
            ' Password=%s;Option=3;'
            % ('172.18.44.5', '3306', 'jydb', 'jydb', '123456'))
req = pyodbc.connect(TGWConnStr)
df = pd.read_sql(data.read(),req)
dataframe = df.set_index(['secucode'])
dictionary = dataframe.to_dict(orient='dict')
del dictionary['enddate']
del dictionary['UpdateTime']
del dictionary['CSRCInduCategory']
del dictionary['report']
del dictionary['OperatingProfit']
del dictionary['ARTRate']

newdict = {}
for item in dictionary.keys():
    values = dictionary.get(item)
    newdict[item] = values.get('600036')
data.close()
# print(newdict)
for key ,values in newdict.items():
    v_dict = dict.get(key.lower())
    try:
        if abs(v_dict-values) >= 0.1:
            print(key,'data not correct')
    except Exception as e:
        print(key,'is null')