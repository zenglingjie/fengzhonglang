from autocase.autoTestcase import interface



def operatingRevenue_TTM():

    inter = interface.interFace('operatingRevenue_TTM','2017-09-20',2087.72,54.6205,53.5469,37.5623,334.6201,19.8769,26.8374,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'operatingRevenue_TTM is error')

operatingRevenue_TTM()