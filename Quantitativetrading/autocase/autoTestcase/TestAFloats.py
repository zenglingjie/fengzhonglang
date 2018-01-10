from autocase.autoTestcase import interface



def AFloats():


    inter = interface.interFace('AFloats','2017-09-27',206.2894,18.4231,6.9556,9.8992,25.6279,2.1008,13.8067,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'AFloats is error')

AFloats()