from autocase.autoTestcase import interface


def NPParentCompanyOwners_TTM ():

    inter = interface.interFace('NPParentCompanyOwners_TTM ','2017-09-21',661.09,4.5249,0.0336,0.2286,5.1305,1.6556,1.524,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.9:
            pass
        else:
            print(i,'NPParentCompanyOwners_TTM is error')


NPParentCompanyOwners_TTM()