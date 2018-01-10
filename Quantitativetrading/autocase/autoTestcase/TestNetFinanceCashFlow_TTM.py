from autocase.autoTestcase import interface




def netFinanceCashFlow_TTM():


    inter = interface.interFace('netFinanceCashFlow_TTM','2017-03-31',791.48,-0.8744,-0.8401,-1.4881,18.7184,-0.6131,-1.1973,100000000)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'netFinanceCashFlow_TTM is error')


netFinanceCashFlow_TTM()