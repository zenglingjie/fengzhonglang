import tushare as ts
import pandas as pd
import requests
import json
import numpy as np

def totalProfit_YOY():
    req = ts.get_stock_basics()
    response = req['profit']
    tushare = response[0:10]
    print(tushare)
    tushare_ = pd.DataFrame(tushare)
    array = np.array(tushare_)
    list = array.tolist()
    list_1 = sum(list, [])
    print(list_1)

    url = 'http://172.17.14.105:8004/test/getfactor'
    values = json.dumps({'codes': ["600036.SH", "600569.SH", "002176.SZ", "002194.SZ", "300312.SZ", "300706.SZ",
                                   "300597.SZ", "603501.SH", "000001.SZ", "601003.SH"],"dateE": "2017-05-03", "factors": [{'name': 'totalProfit_YOY'}]})
    headers = {"Content-type": "application/json"}
    request = requests.Session()
    request.headers.update(headers)
    req = request.post(url, data=values).text
    json_test = json.loads(req)
    data_test = json_test['datas']
    data_test_ = sum(data_test, [])
    print(data_test_)
    tenNumber = []
    for i in range(0, 10):
        number = data_test_[i] / 1
        tenNumber.append(round(number, 2))
    print(tenNumber)

    for i in range(0, 10):
        if abs(list_1[i] - tenNumber[i]) == 0:
            pass
        else:
            print(i, 'totalProfit_YOY is error')


totalProfit_YOY()
