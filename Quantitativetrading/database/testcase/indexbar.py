import tushare as ts
import pandas as pd
import pyodbc
import numpy as np

def indexbar():
    tushare = ts.get_hist_data(code='hs300', start='2016-05-23', end='2017-07-14')

    TGWConnStr = (
        'Driver={MySQL ODBC 5.1 Driver};Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
        % ('172.18.44.122', '3306', 'alphaH', 'testuser', 'test@tgw88'))

    req = pyodbc.connect(TGWConnStr)
    df = pd.read_sql('select * from indexbar where indexcode="000300.SH"',req)
    print(df)
    alphaH = df.set_index(['date'])


    for key, values in tushare.iterrows():
        _date = np.datetime64(key)
        try:
            v_alphaH = alphaH.loc[_date]
            if abs(v_alphaH['open'] - values['open']) >= 0.009:
                print(key, "open data not correct")
            elif abs(v_alphaH['close'] - values['close']) >=0.009:
                print(key,"close data not correct")
            elif abs(v_alphaH['high'] - values['high']) >=0.009:
                print(key,"high data not correct")
            elif abs(v_alphaH['low'] - values['low']) >=0.009:
                print(key,"low data not correct")
            elif abs(v_alphaH['volume'] - values['volume']*100) >=1000:
                print(key,'volume data not correct')
        except Exception as e:
            print(key, "not in alphaH")



indexbar()