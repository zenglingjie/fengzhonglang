from autocase.autoTestcase import interface



def administrationExpense_TTM():


    inter = interface.interFace('administrationExpense_TTM','2017-05-02',0,1.2699,0.5630,0.4386,1.0582,0.2170,0.5753,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'administrationExpense_TTM is error')

administrationExpense_TTM()