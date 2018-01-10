from autocase.autoTestcase import interface


def totalAssetTRate_Q():

    inter = interface.interFace('totalAssetTRate_Q','2017-09-15',0.02,0.32,0.26,0.31,0.87,0.21,0.13,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.01:
            pass
        else:
            print(i,'totalAssetTRate_Q is error')

totalAssetTRate_Q()