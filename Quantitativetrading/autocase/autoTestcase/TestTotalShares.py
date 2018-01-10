import tushare as ts
import json
import requests
import pandas as pd
import numpy as np

def totalShares():
    req = ts.get_stock_basics()
    response = req['totals']
    tushare = response[0:10]
    print(tushare)
    tushare_ = pd.DataFrame(tushare)
    array = np.array(tushare_)
    list = array.tolist()
    list_1 =sum(list,[])
    print(type(array))
    print(list_1)


    url = 'http://172.17.14.105:8004/test/getfactor'
    values = json.dumps({'codes': ["603363.SH","300706.SZ","300654.SZ","603533.SH","002765.SZ","603055.SH","002893.SZ","300527.SZ","601011.SH","603321.SH"], "dateB": "2017-09-12", "dateE": "2017-09-12", "factors": [{'name': 'totalShares'}]})
    headers = {"Content-type": "application/json"}
    request = requests.Session()
    request.headers.update(headers)
    req = request.post(url, data=values).text
    json_test = json.loads(req)
    data_test = json_test['datas']
    data_test_ = sum(data_test,[])
    # print(data_test_)
    tenNumber = []
    for i in range(0,10):
        number = data_test_[i]/100000000
        tenNumber.append(round(number,2))
    print(tenNumber)

    for i in range(0,10):
        if abs(list_1[i]-tenNumber[i])==0:
            pass
        else:
            print(i,'totalShares is error')

totalShares()