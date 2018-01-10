from autocase.autoTestcase import interface



def assetImpairmentLoss_TTM():

    inter = interface.interFace('assetImpairmentLoss_TTM','2017-05-25',173.15,0.0086,0.0171,0,0,0.0080,-0.5278,100000000)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'assetImpairmentLoss_TTM is error')

assetImpairmentLoss_TTM()