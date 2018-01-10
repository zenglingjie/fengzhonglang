from autocase.autoTestcase import interface



def operatingCostRate_Q():

    inter = interface.interFace('operatingCostRate_Q','2017-03-31',0,10.8736,9.1830,7.2602,86.4735,3.9636,2.6047,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'operatingCostRate_Q is error')

operatingCostRate_Q()