from autocase.autoTestcase import interface



def ROE_Q():
    inter = interface.interFace('ROE_Q','2017-09-15',4.75,1.85,-1.79,0.03,4.19,1.79,1.20,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=1:
            pass
        else:
            print(i,'ROE_Q is error')

ROE_Q()
