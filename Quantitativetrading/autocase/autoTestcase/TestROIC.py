from autocase.autoTestcase import interface



def ROIC():


    inter = interface.interFace('ROIC','2017-03-31',0,1.3907,-0.4248,0.0173,1.1666,1.3311,0.7434,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'ROIC is error')


ROIC()