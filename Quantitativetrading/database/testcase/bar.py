import tushare as ts
import pyodbc
import pandas as pd
import numpy as np



def bar():
    tushare = ts.get_hist_data(code='000014',start='2014-07-21',end='2017-06-27')
    print(tushare)
    TGWConnStr = (
        'Driver={MySQL ODBC 5.1 Driver};Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
        % ('172.18.44.122', '3306', 'alphaH', 'testuser', 'test@tgw88'))

    req = pyodbc.connect(TGWConnStr)
    df = pd.read_sql("select * from bar where DATE >='2014-07-21' and DATE <='2017-06-27' and CODE = '000014.XSHE'", req)
    alphaH = df.set_index(['date'])

    for key, values in tushare.iterrows():
        _date = np.datetime64(key)
        try:
            v_alphaH = alphaH.loc[_date]
            if abs(v_alphaH['open'] - values['open']) >= 0.009:
                print(key, "open data not correct")
            elif abs(v_alphaH['close'] - values['close']) >= 0.009:
                print(key, "close data not correct")
            elif abs(v_alphaH['high'] - values['high']) >= 0.009:
                print(key, "high data not correct")
            elif abs(v_alphaH['low'] - values['low']) >= 0.009:
                print(key, "low data not correct")
            elif abs(v_alphaH['volume'] - values['volume']) >= 0.009:
                print(key,'volumn data not correct')
            elif abs(v_alphaH['turnover'] - values['turnover']) >= 0.009:
                print(key,'turnover data not correct')
        except Exception as e:
            print(key, "not in alphaH")

bar()