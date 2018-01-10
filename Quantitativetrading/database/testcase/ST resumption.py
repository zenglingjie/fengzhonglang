import tushare as ts
import pyodbc
import pandas as pd

tushare = ts.get_st_classified()#风险警示板分类
tushare_1 = ts.get_terminated()#终止上市股票列表
tushare_2 = ts.get_suspended()#暂停上市股票列表



def classified():

    tushare = ts.get_st_classified()#风险警示板分类

    TGWConnStr = (
        '={MySQL ODBC 5.1 };Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
        % ('172.18.44.122', '3306', 'alphaH', 'testuser', 'test@tgw88'))

    req = pyodbc.connect(TGWConnStr)
    alphaH = pd.read_sql('select * from ST', req)

    for code, name in tushare.iterrows():
        try:
            if code not in alphaH:
                print(code, ' not in alphaH')
                continue
            elif name not in alphaH:
                print(name, 'not in alphaH')
        except Exception as e:
            print("pass")

