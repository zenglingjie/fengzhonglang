from autocase.autoTestcase import interface



def netProfitParent_YOY ():


    inter = interface.interFace('netProfitParent_YOY','2017-03-31',16.27,0.022,0,0.2916,1.8718,1.2316,0.0863,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'netProfitParent_YOY is error')

netProfitParent_YOY()