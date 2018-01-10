from autocase.autoTestcase import interface


def EBIT_TTM():

    inter = interface.interFace('EBIT_TTM','2017-05-02',0,1.177,0,0.2063,2.8457,0.8944,0.6715,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'EBIT_TTM is error')

EBIT_TTM()