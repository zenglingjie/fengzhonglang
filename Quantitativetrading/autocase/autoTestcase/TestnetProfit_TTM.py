from autocase.autoTestcase import interface



def netProfit_TTM ():


    inter = interface.interFace('netProfit_TTM','2017-09-21',661.09,4.5249,0.0336,0.2286,5.1305,1.6556,1.5240,100000000)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'netProfit_TTM is error')

netProfit_TTM()