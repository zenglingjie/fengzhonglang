import numpy as np
import tushare as ts
import json
import requests

def EMAFun(inputPrice,index):
    for forloopindex in range(0,len(inputPrice)):
        if forloopindex == 0:
            EMA = [(inputPrice)[forloopindex]]
        else:
            EMA.append(EMA[forloopindex - 1] * (index - 1) / (index + 1) + (inputPrice)[forloopindex] * 2 / (index + 1))
    EMA = np.array(EMA)
    return EMA

code = ts.get_h_data(code='000001',start='2017-05-02',end='2017-09-20',autype=None)#时间2个月以上
a = code['close'].values
TargetPrice = list(reversed(a))

TargetDif = EMAFun(TargetPrice,12) - EMAFun(TargetPrice,26)
TargetDEA = EMAFun(TargetDif,9)
TargetBar = TargetDif - TargetDEA
TargetMACD =2 * (TargetDif - TargetDEA)
# print(TargetDif)
# print(TargetDEA)
# print(TargetMACD)#后面往前面看


url = 'http://172.17.14.105:8004/test/getfactor'
values = json.dumps({'codes': ["600036.SH"], "dateB":"2017-05-02","dateE":"2017-09-20", "factors": [{'name':'MACD'}]})
headers = {"Content-type": "application/json"}
request = requests.Session()
request.headers.update(headers)
req = request.post(url, data=values).text
json_test = json.loads(req)
data_test = json_test['datas']
data_test_ = sum(data_test, [])
print(len(data_test_))
print(data_test_)
# tenNumber = []
# for i in range(0, 100):
#     number = data_test_[i] / 1
#     tenNumber.append(round(number, 3))

