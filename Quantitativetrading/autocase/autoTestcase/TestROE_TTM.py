from autocase.autoTestcase import interface

def ROE_TTM():

    inter = interface.interFace('ROE_TTM','2017-09-19',15.7636,9.0359,0.2603,0.7893,10.2003,5.1307,4.0434,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i]<=0.9):
            pass
        else:
            print(i,'ROE_TTM is error')


ROE_TTM()