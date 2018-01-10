from autocase.autoTestcase import interface



def netProfit_parent_Q ():

    inter = interface.interFace('netProfit_parent_Q','2017-05-03',199.77,0.9205,0,0.0078,2.0260,0.5701,0.4535,100000000)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'netProfit_parent_Q is error')

netProfit_parent_Q()