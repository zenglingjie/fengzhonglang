import json
import requests

class interFace(object):

    def __init__(self,name,time,ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7,number):
        self.name = name
        self.time = time
        self.ticket_1 = ticket_1
        self.ticket_2 = ticket_2
        self.ticket_3 = ticket_3
        self.ticket_4 = ticket_4
        self.ticket_5 = ticket_5
        self.ticket_6 = ticket_6
        self.ticket_7 = ticket_7
        self.number = number


    def factor_interface(self):

        url = 'http://172.17.14.105:8004/test/getfactor'
        values = json.dumps({'codes': ["600036.SH", "002239.SZ", "000868.SZ", "600792.SH", "601003.SH", "002109.SZ",
                                       "002176.SZ"], "dateE": self.time, "factors": [{'name': self.name}]})
        headers = {"Content-type": "application/json"}
        request = requests.Session()
        request.headers.update(headers)
        req = request.post(url, data=values).text
        json_test = json.loads(req)
        data_test = json_test['datas']
        data_test_ = sum(data_test, [])
        # print(data_test_)
        try:
            tenNumber = []
            for i in range(0, 7):
                if data_test_[i] is None:
                    print(data_test_[i],'object is error')
                    raise NameError
                elif data_test_[i] is not None:
                    number = data_test_[i] / self.number
                    tenNumber.append(round(number, 2))
        except TypeError:
            print('object is error')
        return tenNumber

    def ticket_pool(self):


        ticket_1 = self.ticket_1  # 600036
        ticket_2 = self.ticket_2  # 002239
        ticket_3 = self.ticket_3  # 000868
        ticket_4 = self.ticket_4  # 600792
        ticket_5 = self.ticket_5  # 601003
        ticket_6 = self.ticket_6  # 002109
        ticket_7 = self.ticket_7  # 002176

        ticket_all = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7]
        all_ = []
        for x in range(0, 7):
            number = ticket_all[x] / 1
            all_.append(round(number, 3))
        return all_

if __name__ == '__main__':
    a = interFace('totalAssetTRate_Q','2017-09-15',0.02,0.32,0.26,0.31,0.87,0.21,0.13,1)
    a.factor_interface()


