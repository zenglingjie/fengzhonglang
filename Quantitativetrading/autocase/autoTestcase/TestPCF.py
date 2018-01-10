from autocase.autoTestcase import interface



def PCF():

    inter = interface.interFace('PCF','2017-09-26',-5.84,52.64,3.66,3.90,4.78,17.09,-25.52,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'PCF is error')

PCF()