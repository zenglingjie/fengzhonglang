from autocase.autoTestcase import interface



def operatingProfit_Q():

    inter = interface.interFace('operatingProfit_Q','2017-05-02',253.24,1.045,-0.5064,-0.0420,1.9725,0.7632,0.4455,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'operatingProfit_Q is error')

operatingProfit_Q()