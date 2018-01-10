# __*__coding=utf-8__*__
import pyodbc
import tushare as ts

data = ts.get_stock_basics()
code = data['name'].values

TGWConnStr = (
    '={MySQL ODBC 5.1 };Server=%s;Port=%s;Database=%s;User=%s; Password=%s;Option=3;'
     % ('172.18.44.122', '3306', 'alphaH', 'testuser', 'test@tgw88'))

req = pyodbc.connect(TGWConnStr)
sur = req.cursor()
res = sur.execute('select abbr from secumain')
a = []
for ros in res:
    a.append(ros[0])














