from autocase.autoTestcase import interface


def ROE_YOY():

    inter = interface.interFace('ROE_YOY','2017-09-15',0.0453,-0.7604,-3.7191,-1.4374,6.1165,7.8782,-0.6623,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())
    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.1:
            pass
        else:
            print(i,'ROE_YOY is error')

ROE_YOY()

