from autocase.autoTestcase import interface




def grossProfit_TTM():

    inter = interface.interFace('grossProfit_TTM','2017-09-20',0,2.9575,0.6787,0.5560,3.973,1.1812,0.9248,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'grossProfit_TTM is error')

grossProfit_TTM()