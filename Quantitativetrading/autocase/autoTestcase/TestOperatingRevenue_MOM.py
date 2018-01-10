from autocase.autoTestcase import interface


def operatingRevenue_MOM():

    inter = interface.interFace('operatingRevenue_MOM','2017-09-15',-2.6,-5.65,41.0, 35.14,11.11,-18.55,89.22,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'operatingRevenue_MOM is error')


operatingRevenue_MOM()