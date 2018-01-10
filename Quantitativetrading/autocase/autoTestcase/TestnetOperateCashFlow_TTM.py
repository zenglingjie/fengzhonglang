from autocase.autoTestcase import interface



def netOperateCashFlow_TTM():


    inter = interface.interFace('netOperateCashFlow_TTM','2017-03-31',-2143,0.5059,-2.5347,2.0941,-6.5929,0.4611,-2.7543,100000000)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'netOperateCashFlow_TTM is error')

netOperateCashFlow_TTM()