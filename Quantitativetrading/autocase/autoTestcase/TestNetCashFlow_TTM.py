from autocase.autoTestcase import interface



def netCashFlow_TTM():


    inter = interface.interFace('netCashFlow_TTM','2017-03-31',-2309,1,1,1,1,1,1,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'netCashFlow_TTM is error')

netCashFlow_TTM()