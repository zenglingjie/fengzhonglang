import tushare as ts
import pandas as pd
import pyodbc
from datetime import *
import numpy as np
tushare = ts.get_hist_data(code='hs300', start='2016-05-23', end='2017-07-14')

TGWConnStr = (
    'Driver={MySQL ODBC 5.1 Driver};Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
    % ('172.18.44.122', '3306', 'alphaH', 'testuser', 'test@tgw88'))

req = pyodbc.connect(TGWConnStr)
df = pd.read_sql('select * from indexbar where indexcode="000300.XSHG"',req)
alphaH = df.set_index(['date'])

for key, values in tushare.iterrows():
    _date = np.datetime64(key)
    try:
        v_alphaH = alphaH.loc[_date]
        if abs(v_alphaH['open'] - values['open']) >= 0.009:
            print(key, "data not correct")
    except Exception as e:
        print(key, "not in datelist")


