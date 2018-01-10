from autocase.autoTestcase import interface

def totalMV():

    int = interface.interFace("totalMV",'2017-09-18',5314,163,57.9,57.7,190,66.6,246,100000000)
    print(int.factor_interface())
    print(int.ticket_pool())
    for i in range(0,7):
        if abs(int.factor_interface()[i]-int.ticket_pool()[i])<=0.9:
            pass
        else:
            print(i,'totalMV is error')

totalMV()