import tushare as ts
import pandas as pd
import pyodbc

code = ts.get_hist_data(code='hs300',start='2016-05-23',end='2017-07-14')

tushare ={}
for index,row in code.iterrows():
    tushare[index] = (row['open'])

TGWConnStr = (
    'Driver={MySQL ODBC 5.1 Driver};Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
    % ('172.18.44.122', '3306', 'alphaH', 'testuser', 'test@tgw88'))

req = pyodbc.connect(TGWConnStr)
df = pd.read_sql('select * from indexbar',req)
datelist = df.set_index(['date'])

alphaH = {}
for index, row in datelist.iterrows():
    alphaH[index.to_pydatetime().strftime('%Y-%m-%d')] = row['open']


for key, values in tushare.items():
    if key not in alphaH:
        print(key, "not in alphaH")
        continue

    v_alphaH = alphaH.get(key)
    try:
        if abs(v_alphaH - values) >= 0.009:
            print(key, "data not correct")
    except Exception as e:
        import traceback
        traceback.print_exc()