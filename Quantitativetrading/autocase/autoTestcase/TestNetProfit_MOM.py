from autocase.autoTestcase import interface



def netProfit_MOM():

    inter = interface.interFace('netProfit_MOM','2017-06-30',168.81,0.8829,0.0911,0,0.6357,0.2873,0.7026,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'netProfit_MOM is error')

netProfit_MOM()