from autocase.autoTestcase import interface



def PB():

    inter = interface.interFace('PB','2017-09-20',1.56,3.32,4.48,2.07,3.77,2.00,6.79,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.19:
            pass
        else:
            print(i,'PB is error')


PB()