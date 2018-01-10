from autocase.autoTestcase import interface



def basicEPS_YOY():

    inter = interface.interFace('basicEPS_YOY','2017-05-02',0.0600,0,0,0.0220,0.0731,0.1630,0.0020,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'basicEPS_YOY is error')

basicEPS_YOY()