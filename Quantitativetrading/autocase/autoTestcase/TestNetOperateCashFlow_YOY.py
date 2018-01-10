from autocase.autoTestcase import interface




def netOperateCashFlow_YOY():

    inter = interface.interFace('netOperateCashFlow_YOY','2017-03-31',726.89,0.2655,2.5267,2.2235,0,0.4248,0,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'netOperateCashFlow_YOY is error')

netOperateCashFlow_YOY()