from db.com.readConfig import *
from db.com.testTushare import *
import json


class TestAllCase(object):
    def __init__(self):
        self.config_list = ReadConfig.read_file()

    def each_case(self):
        for config in self.config_list:
            config_dic = json.loads(config)
            data_get_bar = DataGetBarTestCase(config_dic)
            data_get_bar.run()

if __name__ == "__main__":
    obj = TestAllCase()
    obj.each_case()

