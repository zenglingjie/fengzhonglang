from autocase.autoTestcase import interface


def ROA_TTM():

    inter = interface.interFace('ROA_TTM','2017-09-15',1.101,5.5777,-0.2636,-0.9138,2.3454,5.8519,2.1597,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'ROA_TTM is error')

ROA_TTM()