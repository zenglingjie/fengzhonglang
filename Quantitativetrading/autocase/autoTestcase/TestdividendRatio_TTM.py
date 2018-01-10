from autocase.autoTestcase import interface




def dividendRatio_TTM():

    inter = interface.interFace('dividendRatio_TTM','2017-09-26',4.2045,0.3824,0,0,0.6303,0,0.1174,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'dividendRatio_TTM is error')


dividendRatio_TTM()