import requests
import tushare as ts

tushare = ts.get_hist_data(code='000001',start='2017-01-13',end='2017-01-18')
print(tushare['open'].to_json(orient='columns'))
print(type(tushare))

url = 'http://172.18.44.123:8004/history/getindexbar'#取指数行情
values = {"codes": ["000001.SZ"], "dateB": "2017-01-13", "dateE": "2017-01-18", "type": "normal", "fields": ["open"]}#取指数行情

url_1 = 'http://172.18.44.123:8004/main/getsecu'#取证券主表
url_2 = 'http://172.18.44.123:8004/main/getindex'#指数主表
url_3 = 'http://172.18.44.123:8004/main/getindustry'#行业主表接口

url_4 = 'http://172.18.44.123:8004/component/getindex'#取指数成分
values_4 = {"codes":["000001.SH","000300.SH"],"dateB":"2017-01-13","dateE":"2017-01-18"}#取指数成分

url_5 = 'http://172.18.44.123:8004/component/getind'#取行业成分
values_5 ={"codes":["3540_CITIC","3520_CITIC"],"dateB":"2016-01-05","dateE":"2016-01-18"}#取行业成分

url_6 = 'http://localhost:8004/v/ST'#取ST
values_6 = {"dateB":"1990-01-01","dateE":"2017-08-15"}#取ST

url_7 = 'http://172.18.44.123:8004/v/suspended'#取停复牌
values_7 = {"codes":["000669.SZ","601388.SH"],"dateB":"2016-02-01","dateE":"2016-02-02"}#取停复牌

url_8 = 'http://172.18.44.123:8004/v/dividend'#取分红
values_8 = {"codes":["000669.SZ","601388.SH"]}#取分红

url_9 = 'http://172.18.44.123:8004/v/split'#取送股
values_9 = {"codes":["000669.SZ","601388.SH"]}#取送股

url_10 ='http://172.18.44.123:8004/test/getfactor'#取MACD
values_10 = {"name":"getfactor","codes":["000001.SZ"],"dateB":"2017-01-13","dateE":"2017-01-18","factors":[{"name":"MACD_DIF","params":{"dif_s":12,"dif_l":26}},{"name":"MACD_DEA","params":{"dif_s":12,"dif_l":26,"dea":9}},{"name":"MACD_HIST","params":{"dif_s":12,"dif_l":26,"dea":9}}]}#取MACD




