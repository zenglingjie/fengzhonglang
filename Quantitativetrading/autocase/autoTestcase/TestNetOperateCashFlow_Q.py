from autocase.autoTestcase import interface




def netOperateCashFlow_Q():

    inter = interface.interFace('netOperateCashFlow_Q','2017-05-02',-2143.5,0.51,-2.53,2.09,-6.59,0.46,-2.75,100000000)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'netOperateCashFlow_Q is error')


netOperateCashFlow_Q()