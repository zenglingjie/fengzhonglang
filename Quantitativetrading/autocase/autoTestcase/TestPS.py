from autocase.autoTestcase import interface



def PS():

    inter = interface.interFace('PS','2017-09-19',2.90,3.09,1.22,1.63,0.50,3.46,12.54,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'PS is error')

PS()