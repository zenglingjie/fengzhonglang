import numpy as np
import tushare as ts
import matplotlib.pyplot as plt


code = ts.get_h_data(code='000002',start='2016-10-01',end='2017-01-13',autype=None)
a = code['close'].values
TargetPrice = list(reversed(a))

# The inputPrice is a dataframe that averageprice and closepriceare included
### EMA Function
def EMAFun(inputPrice,index):
    for forloopindex in range(0,len(inputPrice)):
        if forloopindex == 0:
            EMA = [(inputPrice)[forloopindex]]
        else:
            EMA.append(EMA[forloopindex - 1] * (index - 1) / (index + 1) + (inputPrice)[forloopindex] * 2 / (index + 1))
    EMA = np.array(EMA)
    return EMA

TargetDif = EMAFun(TargetPrice,12) - EMAFun(TargetPrice,26)
TargetDEA = EMAFun(TargetDif,9)
TargetBar = TargetDif - TargetDEA
TargetMACD =2 * (TargetDif - TargetDEA)

# fig = plt.figure(figsize=[18,5])
# plt.plot(code.index,TargetDif,label='TargetDif')
# plt.plot(code.index,TargetDEA,label='TargetDEA')
# plt.plot(code.index,TargetMACD,label='TargetMACD')

#plt.show()
print(TargetDif)
print(TargetDEA)
print(TargetMACD)


