import tushare as ts
import json
import requests


def TestPE_TTM():
    tushare_2 = ts.get_h_data(code='600036',start='2017-08-22',end='2017-09-10',autype='None')
    tushare_1 = ts.get_h_data(code='600036',start='2017-05-01',end='2017-06-22',autype='None')
    tushare_3 = ts.get_h_data(code='600036',start='2015-05-04',end='2015-07-07',autype='None')
    # pe_ttm =股价/前四个季度EPS
    price_3 = tushare_3['close']
    price_2 = tushare_2['close']
    price_1 = tushare_1['close']

    pe_1 = price_1/2.52#前四个季度EPS
    ttm_1 =[]
    for a in pe_1:
        ttm_1.append(a)
    ttm_1_1 = ttm_1[::-1]
    # print(ttm_1_1)
    # print(len(ttm_1[::-1]))
    # print(type(ttm_1))
    pe_2 = price_2/2.62
    ttm_2 = []
    for a in pe_2:
        ttm_2.append(a)
    ttm_2_2 = ttm_2[::-1]
    # print(ttm_2_2)
    # print(len(ttm_2[::-1]))
    # print(type(ttm_2))
    pe_3 = price_3/2.31
    ttm_3 = []
    for a in pe_3:
        ttm_3.append(a)
    ttm_3_3 = ttm_3[::-1]
    # print(ttm_3_3)
    # print(len(ttm_3[::-1]))
    # print(type(ttm_3))
    url = 'http://172.17.14.105:8004/test/getfactor'
    values_2 = json.dumps({'codes':["600036.SH"],"dateB":"2017-08-22","dateE":"2017-09-10","factors":[{'name':'PE_TTM'}]})
    values_1 = json.dumps({'codes':["600036.SH"],"dateB":"2017-05-01","dateE":"2017-06-22","factors":[{'name':'PE_TTM'}]})
    values_3 = json.dumps({'codes':["600036.SH"],"dateB":"2015-05-04","dateE":"2015-07-07","factors":[{'name':'PE_TTM'}]})
    headers = {"Content-type": "application/json"}
    request = requests.Session()
    request.headers.update(headers)
    req_2 = request.post(url,data=values_2).text
    req_1 = request.post(url,data=values_1).text
    req_3 = request.post(url,data=values_3).text
    json_test_2 = json.loads(req_2)
    data_test_2 = json_test_2['datas']
    json_test_1 = json.loads(req_1)
    data_test_1 = json_test_1['datas']
    json_test_3 = json.loads(req_3)
    data_test_3 = json_test_3['datas']


    data_test_1_1 = sum(data_test_1,[])
    # print(data_test_1_1)
    # print(len(data_test_1_1))
    # print(type(data_test_1_1))
    data_test_2_2 = sum(data_test_2,[])
    data_test_3_3 = sum(data_test_3,[])

    for i in range(0,36):
        if abs(ttm_1_1[i]-data_test_1_1[i])<=0.04:
            pass
        else:
            print(i,'pe_ttm is error')

    for i in range(0,14):
        if abs(ttm_2_2[i]-data_test_2_2[i])<=0.04:
            pass
        else:
            print(i,'pe_ttm is error')

    for i in range(0,46):
        if abs(ttm_3_3[i] - data_test_3_3[i]) <= 0.04:
            pass
        else:
            print(i,'pe_ttm is error')

TestPE_TTM()

