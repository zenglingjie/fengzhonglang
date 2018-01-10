from autocase.autoTestcase import interface




def NAPS():

    inter = interface.interFace('NAPS','2017-05-02',16.68,4.46,1.87,3.01,1.89,4.53,2.57,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'NAPS is error')


NAPS()