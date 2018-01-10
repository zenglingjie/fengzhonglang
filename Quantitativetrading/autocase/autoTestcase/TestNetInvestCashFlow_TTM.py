from autocase.autoTestcase import interface



def netInvestCashFlow_TTM():

    inter = interface.interFace('netInvestCashFlow_TTM','2017-06-30',-953,-0.4367,-0.2201,-0.0126,-0.0359,-0.0037,0.5398,100000000)#找不到
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'netInvestCashFlow_TTM is error')


netInvestCashFlow_TTM()