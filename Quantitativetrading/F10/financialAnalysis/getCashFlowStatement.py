#现金流量表
import requests
import pyodbc
import pandas as pd

#接口请求
content = {'secuCode':'000725', 'totalType': 1, 'subType': 3 ,'beginIndex': 0, 'recordNum': 10}
response = requests.get(url='http://172.18.44.120:8050/financial-analysis/stocksData/financialAnalysis/getCashFlowStatement',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
del dict['id']
del dict['updatetime']
del dict['secucode']
del dict['totaltype']
del dict['subtype']
del dict['time']
del dict['iscompared']
del dict['industrytype']
print(dict)
print(value_)


#数据库请求
data = open('F:/Quantitativetrading/F10/sql/getCashFlowStatement.txt', 'r+',encoding='utf-8')
TGWConnStr = ('Driver={MySQL ODBC 5.3 Unicode Driver};'
            'Server=%s;Port=%s;'
            'Database=%s;User=%s;'
            ' Password=%s;Option=3;'
            % ('172.18.44.115', '3306', 'jydb', 'jydb', '123456'))
req = pyodbc.connect(TGWConnStr)
df = pd.read_sql(data.read(),req)
dataframe = df.set_index(['secucode'])
dictionary = dataframe.to_dict(orient='dict')
del dictionary['CSRCInduCategory']
del dictionary['report']
del dictionary['comparetype']
del dictionary['UpdateTime']
del dictionary['enddate']
del dictionary['datatype']
del dictionary['dictionary']

newdict = {}
for item in dictionary.keys():
    values = dictionary.get(item)
    newdict[item] = values.get('000725')
data.close()
print(newdict)
for key ,values in newdict.items():
    v_dict = dict.get(key.lower())
    try:
        if abs(v_dict-values) >= 0.1:
            print(key,'data not correct')
    except Exception as e:
        print(key,'is null')