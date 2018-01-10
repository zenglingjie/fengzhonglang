import requests
import tushare as ts
import json
import operator


class DataGetBarTestCase(object):
    def __init__(self, config):
        self.url = config["url"]
        self.values = config["values"]
        self.ts_get_data = config["tushare"]
        self.describe = config["describe"]
        self.headers = {"Content-type": "application/json"}

        # self.url = 'http://172.18.44.123:8004/history/getbar'
        #
        # self.values = {"codes": ["000001.SZ"], "dateB": "2016-01-13", "dateE": "2017-01-18", "type": "normal",
        #                "fields": ["open", "close"]}

    def get_every_code_data(self):
        if self.values:
            values = self.values
            start_values = values["dateB"]
            if "dateE" in values:
                end_values = values["dateE"]
            else:
                end_values = start_values
            codes_values = values["codes"]
            fields_values = values["fields"]
            for code in codes_values:
                for field in fields_values:
                    open_tushare, date_ts_list = self.get_tushare_data(code[:6], start_values, end_values, field)
                    open_test, date_test_list = self.get_test_data(self.url, code, field, values)

                    if operator.eq(len(date_ts_list), len(date_test_list))\
                            and (set(date_ts_list) >= set(date_test_list)) and (set(date_test_list) >= set(date_ts_list)):
                        open_tushare_set = set(open_tushare)
                        open_test_set = set(open_test)
                        if operator.eq(len(open_test), len(open_tushare))\
                                and (open_tushare_set >= open_test_set) and (open_test_set >= open_tushare_set):
                            print(self.describe)
                            print("%s : %s is right" % (code, field))
                            print()
                        else:
                            print(self.describe)
                            print("%s : %s is wrong" % (code, field))
                            print(open_tushare_set - open_test_set)
                            print(open_test_set - open_tushare_set)
                            print()

                    else:
                        print(self.describe)
                        print("%s : %s DATES is wrong" % (code, field))
                        print(set(date_ts_list) ^ set(date_test_list))
                        print()
        else:
            date_ts_list = self.get_tushare_data1()
            date_test_list = self.get_test_data1()

    def get_tushare_data(self,code, start_date, end_date, field):
        # df = ts.get_hist_data(code=code, start=start_date, end=end_date)
        df = eval(self.ts_get_data)

        json_str = df.to_json(orient='columns')
        json_str_split = df.to_json(orient='split')

        data_split = json.loads(json_str_split)
        date_list = data_split["index"]

        data = json.loads(json_str)
        if field == "amount":
            field = "volume"
        field_test = list(data[field].values())
        # field_test.sort()
        return field_test, date_list

    def get_tushare_data1(self):
        # df = ts.get_hist_data(code=code, start=start_date, end=end_date)
        df = eval(self.ts_get_data)

        json_str = df.to_json(orient='columns')
        json_str_split = df.to_json(orient='split')

        data_split = json.loads(json_str_split)
        date_list = data_split["index"]

        data = json.loads(json_str)

        # field_test = list(data[field].values())
        # field_test.sort()
        # print(field_test)
        return date_list

    def get_test_data(self, url, code, field, values):
        if len(values) >= 1:
            values["codes"] = [code]
            values["fields"] = [field]

        s = requests.Session()
        s.headers.update(self.headers)

        r = s.post(url, json=values).text

        json_test = json.loads(r)
        data_test = json_test["datas"]
        date_test_list = json_test["dates"]
        field_test = json_test["fields"]
        open_index = field_test.index(field)
        open_test = data_test[open_index]
        # open_test.sort()
        return open_test, date_test_list

    def get_test_data1(self):
        s = requests.Session()
        s.headers.update(self.headers)

        r = s.post(self.url, json=self.values).text

        json_test = json.loads(r)
        data_test = json_test["datas"]
        date_test_list = json_test["dates"]
        field_test = json_test["fields"]
        # open_index = field_test.index(field)
        # open_test = data_test[open_index]
        # open_test.sort()
        # print(open_test)
        return date_test_list

    def run(self):
        self.get_every_code_data()


if __name__ == "__main__":
    obj = DataGetBarTestCase()
    obj.run()



