from autocase.autoTestcase import interface



def EPS_TTM():

    inter = interface.interFace('EPS_TTM','2017-09-25',2.621,0.145,0.005,0.023,0.200,0.236,0.104,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'EPS_TTM is error')

EPS_TTM()