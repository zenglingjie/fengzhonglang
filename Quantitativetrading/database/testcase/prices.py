import tushare as ts

#票000006
#后复权因子=64.0028
#const为精确复权常数=32.2498
#前复权因子=1.02055


def Ohoufuquan(factor,const):

    code = ts.get_h_data(code='000002', start='2017-04-24', end='2017-04-28', autype='None')
    price = code['open'].values
    print(price)
    open = price * factor + const
    print(open)
    return open

def Choufuquan(factor,const):

    code = ts.get_h_data(code='000002', start='2017-04-25', end='2017-04-25', autype='None')
    price = code['close'].values
    print(price)
    close = price * factor + const
    print(close)
    return close

def Oqianfuquan(factor,const,latest_factor,latest_const):

    code = ts.get_h_data(code='000006',start='2016-06-20',end='2016-06-20',autype='None')
    price = code['open'].values
    print(price)
    open = price * factor/latest_factor + (const - latest_const)/latest_factor
    print(open)
    return open

def Cqianfuquan(factor,const,latest_factor,latest_const):

    code = ts.get_h_data(code='000006',start='2016-06-20',end='2016-06-20',autype='None')
    price = code['close'].values
    print(price)
    close = price * factor/latest_factor + (const - latest_const)/latest_factor
    print(close)
    return close




# Ohoufuquan(factor=64.0028,const=32.2498)
Choufuquan(factor=123.637,const=282.207)
# Oqianfuquan(factor=64.0028,const=32.2498,latest_factor=64.0028,latest_const=43.7703)
# Cqianfuquan(factor=64.0028,const=32.2498,lat_factor=64.0028,latest_const=43.7703)est

