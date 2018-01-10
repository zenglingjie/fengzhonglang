from autocase.autoTestcase import interface



def EPS_Q():

    inter = interface.interFace('EPS_Q','2017-05-02',0.79,0.08,-0.03,0.00,0.08,0.08,0.03,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'EPS_Q is error')

EPS_Q()