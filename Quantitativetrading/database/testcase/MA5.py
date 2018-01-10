import tushare as ts

def date5():
    code = ts.get_hist_data(code='000001',start='2017-05-05',end='2017-05-11')
    a = code['close'].values
    getprice = list(reversed(a))
    #print(getprice)
    #print(len(getprice))
    return getprice


def date10():
    code = ts.get_hist_data(code='000001', start='2017-05-05', end='2017-05-18')
    a = code['close'].values
    getprice = list(reversed(a))
    #print(getprice)
    #print(len(getprice))
    return getprice

def date20():
    code = ts.get_hist_data(code='000001', start='2017-05-05', end='2017-06-02')
    a = code['close'].values
    getprice = list(reversed(a))
    print(getprice)
    print(len(getprice))
    return getprice

def date30():
    code = ts.get_hist_data(code='000001', start='2017-05-05', end='2017-06-16')
    a = code['close'].values
    getprice = list(reversed(a))
    print(getprice)
    print(len(getprice))
    return getprice


def date60():
    code = ts.get_hist_data(code='000001', start='2017-03-21', end='2017-06-16')
    a = code['close'].values
    getprice = list(reversed(a))
    print(getprice)
    print(len(getprice))
    return getprice

def MA(inputPrice,datetime):
    answer = 0
    for x in inputPrice:
        answer = answer + x

    return answer/datetime

def cha():
    if MA(date5(),datetime=5)-MA(date10(),datetime=10)>0:
        print('buy in')
    elif MA(date5(),datetime=5)-MA(date10(),datetime=10)<0:
        print('sell to')
    else:
        print('Half a moment! ')

cha()