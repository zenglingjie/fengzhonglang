from autocase.autoTestcase import interface



def dilutedEPS_YOY():

    inter = interface.interFace('dilutedEPS_YOY','2017-05-02',0.0600,0,0,0.0220,0.0731,0.1630,0.0020,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'dilutedEPS_YOY is error')

dilutedEPS_YOY()