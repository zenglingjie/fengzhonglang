#主要指标
import requests
import pyodbc
import pandas as pd
import collections

#接口请求
code_dict = {'招商银行': 600036, '中国平安': 601318, '京东方A': '000725', '格力电器': '000651', '中科曙光': 603019, '江丰电子': '300666','汇顶科技': '603160'}
codelist =collections.OrderedDict()
codelist = code_dict
for code in codelist.values():
    content = {'secuCode':code, 'type': 0, 'beginIndex': 0, 'recordNum': 10}
    response = requests.get(url='http://172.18.44.120:8050/financial-analysis/stocksData/financialAnalysis/getMainIndicators',params=content)
    answer = response.json()
    value_ = []
    for value in answer.values():
        value_.append(value)
    list_ = list(value_[2])
    dict = list_[0]
    del dict['id']
    del dict['updatetime']
    # del dict['secucode']
    del dict['type']
    del dict['time']
    del dict['industrytype']
    # print(dict)

#数据库请求
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
del dictionary['UpdateTime']
del dictionary['CSRCInduCategory']
del dictionary['report']
del dictionary['enddate']
# print(dictionary)

secumain = collections.OrderedDict()
secumain = code_dict
for data_code in secumain.values():
    data_code_str = str(data_code)
    newdict = {}
    for item in dictionary.keys():
        values = dictionary.get(item)
        newdict[item] = values.get(data_code_str)
    # print(newdict)

for key , values in newdict.items():
    v_dict = dict.get(key.lower())
    try:
        if abs(v_dict-values) >= 0.1:
            print(key,'data not correct')
    except Exception as e:
        print(key,'is None')