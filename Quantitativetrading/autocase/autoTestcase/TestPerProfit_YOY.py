from autocase.autoTestcase import interface



def perProfit_YOY():

    inter = interface.interFace('perProfit_YOY','2017-03-31',45.56,0.1098,7.3504,0.1683,3.185,1.5883,-0.4098,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'perProfit_YOY is error')

perProfit_YOY()