from autocase.autoTestcase import interface



def operatingRevenue_YOY():

    inter = interface.interFace('operatingRevenue_YOY','2017-03-31',-2.53,2.3266,5.9736,3.8106,68.1161,0.4990,-3.0097,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'operatingRevenue_YOY is error')


operatingRevenue_YOY()