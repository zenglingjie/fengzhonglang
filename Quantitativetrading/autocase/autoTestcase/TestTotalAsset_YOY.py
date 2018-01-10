from autocase.autoTestcase import interface
import tushare as ts
import pandas as pd
import numpy as np
import json
import requests



class totalAsset_YOY():


    def __init__(self,time,name):
        self.time = time
        self.name = name

    def tushare_totalAsset_YOY(self):

        tushare = ts.get_growth_data(2017, 2)
        response = tushare['targ']
        tushare = response[0:7]
        tushare_ = pd.DataFrame(tushare)
        array = np.array(tushare_)
        list = array.tolist()
        list_1 = sum(list, [])
        sevenNumber = []
        for i in range(0, 7):
            number = list_1[i] / 1
            sevenNumber.append(round(number, 2))
        print(sevenNumber)
        # codeList = ['600395','002468','600505','000878','002352','600516','603318']

        url = 'http://172.17.14.105:8004/test/getfactor'
        values = json.dumps({'codes': ["600395.SH", "002468.SZ", "600505.SH", "000878.SZ", "002352.SZ", "600516.SH",
                                       "603318.SH"], "dateE": self.time, "factors": [{'name': self.name}]})
        headers = {"Content-type": "application/json"}
        request = requests.Session()
        request.headers.update(headers)
        req = request.post(url, data=values).text
        json_test = json.loads(req)
        data_test = json_test['datas']
        data_test_ = sum(data_test, [])
        # print(data_test_)
        tNumber = []
        for i in range(0, 7):
            number = data_test_[i] / 1
            tNumber.append(round(number, 2))
        print(tNumber)

        for i in range(0,7):
            if abs(sevenNumber[i]-tNumber[i])<=0.1:
                pass
            else:
                print(i,'totalAsset_YOY is error')


if __name__ == '__main__':
    YOY = totalAsset_YOY('2017-09-15','totalAsset_YOY')
    YOY.tushare_totalAsset_YOY()
