from autocase.autoTestcase import interface



def operatingRevenue_Q():

    inter = interface.interFace('operatingRevenue_Q','2017-09-20',555.9,13.05,13.91,10.56,100.5,4.19,6.679,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'operatingRevenue_Q is error')

operatingRevenue_Q()