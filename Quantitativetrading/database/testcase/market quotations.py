import tushare as ts


# 一次性获取全部日k线数据
a = ts.get_hist_data('300015')#爱尔眼科
b = ts.get_hist_data('002166')#莱茵生物
c = ts.get_hist_data('603005')#晶方科技
d = ts.get_hist_data('300235')#方直科技
e = ts.get_hist_data('300123')#太阳鸟
f = ts.get_hist_data('600110')#诺德股份
j = ts.get_hist_data('600466')#蓝光发展
q = ts.get_hist_data('000021')#深科技
w = ts.get_hist_data('000863')#三湘印象
i = ts.get_hist_data('600763')#通策医疗
o = ts.get_hist_data('002184')#海得控制
k = ts.get_hist_data('000009')#中国宝安
m = ts.get_hist_data('000547')#航天发展

mq = {'300015':a ,'002166':b,'603005':c,'300235':d,'300123':e,'600110':f,'600466':j,'000021':q,'000863':w,'600763':i,'002184':o,'000009':k,'000547':m}
for k, v in mq.items():
    v.to_excel('./db/' + k + '.xlsx')






