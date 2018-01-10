import tushare as ts

df = ts.get_stock_basics()
date = df.ix['600848']['timeToMarket'] #上市日期YYYYMMDD

a = ('300015','002166','603005','300235','300123','600110','600466','000021','000863','600763','002184','000009','000547')

b = ts.get_h_data('300015') #前复权
c = ts.get_h_data('002166')
d = ts.get_h_data('603005')
e = ts.get_h_data('300235')
f = ts.get_h_data('300123')
g = ts.get_h_data('600110')
h = ts.get_h_data('600466')
j = ts.get_h_data('000021')
k = ts.get_h_data('000863')
l = ts.get_h_data('600763')
z = ts.get_h_data('002184')
x = ts.get_h_data('000009')
v = ts.get_h_data('000547')

b.to_excel('./db/爱尔眼科300015.xlsx')

ab = ts.get_h_data('300015', autype='hfq') #后复权
bc = ts.get_h_data('002166', autype='hfq')
cc = ts.get_h_data('603005', autype='hfq')
dc = ts.get_h_data('300235', autype='hfq')
ec = ts.get_h_data('300123', autype='hfq')
fc = ts.get_h_data('600110', autype='hfq')
gc = ts.get_h_data('600466', autype='hfq')
oc = ts.get_h_data('000021', autype='hfq')
pc = ts.get_h_data('000863', autype='hfq')
qc = ts.get_h_data('600763', autype='hfq')
zc = ts.get_h_data('002184', autype='hfq')
xc = ts.get_h_data('000009', autype='hfq')
vc = ts.get_h_data('000547', autype='hfq')


qaa=ts.get_h_data('300015', autype=None) #不复权
waa=ts.get_h_data('002166', autype=None)
eaa=ts.get_h_data('603005', autype=None)
raa=ts.get_h_data('300235', autype=None)
taa=ts.get_h_data('300123', autype=None)
yaa=ts.get_h_data('600110', autype=None)
uaa=ts.get_h_data('600466', autype=None)
iaa=ts.get_h_data('000021', autype=None)
oaa=ts.get_h_data('000863', autype=None)
paa=ts.get_h_data('600763', autype=None)
aaa=ts.get_h_data('002184', autype=None)
saa=ts.get_h_data('000009', autype=None)
daa=ts.get_h_data('000547', autype=None)

ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据

ts.get_h_data('399106', index=True) #深圳综合指数

rod = [(a,b,c,d,e,f,g,h,j,k,l,z,x,v),(ab,bc,cc,dc,ec,fc,gc,oc,pc,qc,zc,xc,vc),(qaa,waa,eaa,raa,taa,yaa,uaa,iaa,oaa,paa,aaa,saa,daa)]

print(rod)


