#金融资产负债表
import requests
import pyodbc
import pandas as pd


content = {'secuCode':'000001', 'type': 0, 'beginIndex': 0, 'recordNum': 10}
response = requests.get(url='http://172.18.44.123:8002/stocksData/financialAnalysis/getBalanceSheet',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
print(dict)

data = open('F:/Quantitativetrading/F10/sql/financeSQL.txt', 'r+')
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

newdict = {}
for item in dictionary.keys():
    values = dictionary.get(item)
    newdict[item] = values.get('000001')
data.close()
print(newdict)
for key ,values in newdict.items():
    v_dict = dict.get(key.lower())
    try:
        if abs(v_dict-values) >= 0.1:
            print(key,'data not correct')
    except Exception as e:
        print(key,'is null')