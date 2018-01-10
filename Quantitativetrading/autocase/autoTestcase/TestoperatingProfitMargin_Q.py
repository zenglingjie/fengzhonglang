from autocase.autoTestcase import interface



def operatingProfitMargin_Q():

    inter = interface.interFace('operatingProfitMargin_Q','2017-09-20',44.0026,7.8897,-3.5590,-4.6849,2.0413,14.1467,7.8512,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool())<=0.9:
            pass
        else:
            print(i,'operatingProfitMargin_Q is error')

operatingProfitMargin_Q()