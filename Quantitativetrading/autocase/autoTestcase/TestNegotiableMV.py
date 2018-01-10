from autocase.autoTestcase import interface




def negotiableMV():


    inter = interface.interFace('negotiableMV','2017-09-22',5353.21,92.6681,63.7134,56.3267,178.883,19.5168,206.9626,100000000)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,7):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'negotiableMV is error')


negotiableMV()