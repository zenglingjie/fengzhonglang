from autocase.autoTestcase import interface



def minorityProfit_Q():


    inter = interface.interFace('minorityProfit_Q','2017-05-02',11.9,0.0595,1.395,0.6559,0,0,0.8838,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'minorityProfit_Q is error')

minorityProfit_Q()