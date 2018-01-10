import json
import requests



def totalProfit_ttm():


    ticket_1 = 244#600036
    ticket_2 = 1.073#002239
    ticket_3 = -0.3606#000868
    ticket_4 = -0.7627#600792
    ticket_5 = 1.93#601003
    ticket_6 = 0.5562#002109
    ticket_7 = 0.2165#002176

    totalProfit_ttm = [ticket_1,ticket_2,ticket_3,ticket_4,ticket_5,ticket_6,ticket_7]#利润总额（单季） 盈利
    print(totalProfit_ttm)
    print(type(totalProfit_ttm))

    url = 'http://172.17.14.105:8004/test/getfactor'
    values = json.dumps({'codes': ["600036.SH", "002239.SZ", "000868.SZ", "600792.SH", "601003.SH", "002109.SZ",
                                   "002176.SZ" ], "dateB": "2017-09-13",
                         "dateE": "2017-09-13", "factors": [{'name': 'totalProfit_Q'}]})
    headers = {"Content-type": "application/json"}
    request = requests.Session()
    request.headers.update(headers)
    req = request.post(url, data=values).text
    json_test = json.loads(req)
    data_test = json_test['datas']
    data_test_ = sum(data_test, [])
    # print(data_test_)
    # print(type(data_test_))
    tenNumber = []
    for i in range(0,7):
        number = data_test_[i] / 100000000
        tenNumber.append(round(number, 2))
    print(tenNumber)
    for i in range(0,7):
        if tenNumber[i]-totalProfit_ttm[i]<=0.09:
            pass
        else:
            print(i,'totalProfit_ttm is error')

totalProfit_ttm()
