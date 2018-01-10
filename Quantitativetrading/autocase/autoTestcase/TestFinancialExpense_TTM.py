from autocase.autoTestcase import interface



def financialExpense_TTM():

    inter = interface.interFace('financialExpense_TTM','2017-03-31',0,0.2298,0.4975,0.3317,1.0328,0.2327,0.2913,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.07:
            pass
        else:
            print(i,'financialExpense_TTM is error')

financialExpense_TTM()