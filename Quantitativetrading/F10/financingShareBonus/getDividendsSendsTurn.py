#分红送转
import requests
import pandas as pd
import pyodbc

#接口请求
content = {'secuCode':'600036','beginIndex': 0, 'recordNum': 10}
response = requests.get(url='http://172.18.44.120:8050/financing-share-bonus/stocksData/financingShareBonus/getDividendsSendsTurn',params=content)
answer = response.json()
value_ = []
for value in answer.values():
    value_.append(value)
list_ = list(value_[2])
dict = list_[0]
# del dict['id']
# del dict['secuCode']
# del dict['']
print(value_)

#数据库请求
# data = open('F:/Quantitativetrading/F10/sql/getDividendsSendsTurnSQL.txt', 'r+',encoding='utf-8')
# TGWConnStr = ('Driver={MySQL ODBC 5.3 Unicode Driver};'
#             'Server=%s;Port=%s;'
#             'Database=%s;User=%s;'
#             ' Password=%s;Option=3;'
#             % ('172.18.44.5', '3306', 'jydb', 'jydb', '123456'))
# req = pyodbc.connect(TGWConnStr)
# df = pd.read_sql(data.read(),req)
# dictionary = df.to_dict(orient='dict')
# values = dictionary.values()
# # keys = dictionary.get()
# # print(keys)
# print(values)

# newdict = {}
# for item in dictionary.keys():
#     values = dictionary.get(item)
#     newdict[item] = values.get('000725')
# data.close()
# print(newdict)
# for key ,values in newdict.items():
#     v_dict = dict.get(key.lower())
#     try:
#         if abs(v_dict-values) >= 0.1:
#             print(key,'data not correct')
#     except Exception as e:
#         print(key,'is null')