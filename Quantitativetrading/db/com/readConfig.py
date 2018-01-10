import json
from db.com.testTushare import *


class ReadConfig(object):
    def __init__(self):
        pass

    def read_file(self):
        config_list = []
        file_object = open('E:\\Quantitativetrading\\db\\com\\test.conf', 'rb')
        try:
            for line in file_object:
                line = bytes.decode(line)
                if line.strip() != "":
                    json_test = json.loads(line)
                    config_list.append(json_test)
            return config_list
        finally:
            file_object.close()

    def each_case(self):
        config_list = self.read_file()
        for config in config_list:
            data_get_bar = DataGetBarTestCase(config)
            data_get_bar.run()

if __name__ == "__main__":
    obj = ReadConfig()
    obj.each_case()