import tushare as ts


#all = ts.get_today_all()
#all.to_csv('E:/Quantitativetrading/jide_code/testcase/db/当天所有行情.csv')

#req = ts.get_stock_basics()
#req.to_csv('E:/Quantitativetrading/jide_code/testcase/db/所有股票列表.csv')


a=ts.get_hist_data('sh') #获取上证指数k线数据
b=ts.get_hist_data('sz') #获取深圳成指k线数据
c=ts.get_hist_data('hs300') #获取沪深300指数k线数据
d=ts.get_hist_data('sz50') #获取上证50指数k线数据
e=ts.get_hist_data('zxb') #获取中小板指数k线数据
f=ts.get_hist_data('cyb') #获取创业板指数k线数据


a.to_csv('E:/Quantitativetrading/jide_code/testcase/db/获取上证指数k线数据.csv')
b.to_csv('E:/Quantitativetrading/jide_code/testcase/db/获取深圳成指k线数据.csv')
c.to_csv('E:/Quantitativetrading/jide_code/testcase/db/获取沪深300指数k线数据.csv')
d.to_csv('E:/Quantitativetrading/jide_code/testcase/db/获取上证50指数k线数据.csv')
e.to_csv('E:/Quantitativetrading/jide_code/testcase/db/获取中小板指数k线数据.csv')
f.to_csv('E:/Quantitativetrading/jide_code/testcase/db/获取创业板指数k线数据.csv')