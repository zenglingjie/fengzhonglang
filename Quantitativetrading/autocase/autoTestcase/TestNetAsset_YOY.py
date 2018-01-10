from autocase.autoTestcase import interface




def netAsset_YOY():


    inter = interface.interFace('netAsset_YOY','2017-03-31',414.94,10.6177,0.0632,2.4269,3.8397,21.8749,0,1)
    print(inter.ticket_pool())
    print(inter.factor_interface())

    for i in range(0,6):
        if abs(inter.factor_interface()[i]-inter.ticket_pool()[i])<=0.09:
            pass
        else:
            print(i,'netAsset_YOY is error')

netAsset_YOY()