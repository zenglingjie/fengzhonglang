from autocase.autoTestcase import interface




def operatingProfit_TTM():

    inter = interface.interFace('operatingProfit_TTM','2017-03-31',495.76,2.1208,-0.8458,-0.861,3.8978,1.3205,0.8014,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'operatingProfit_TTM is error')

operatingProfit_TTM()