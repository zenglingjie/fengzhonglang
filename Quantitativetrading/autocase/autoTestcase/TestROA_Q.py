from autocase.autoTestcase import interface



def ROA_Q():

    inter = interface.interFace('ROA_Q','2017-09-18',0.3136,1.08,-0.2528,-1.2942,0.9008,1.001,0.1981,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for x in range(0,7):
        if abs(inter.factor_interface()[x]-inter.ticket_pool()[x])<0.09:
            pass
        else:
            print(x,'ROA_Q is error')


ROA_Q()