from autocase.autoTestcase import interface


def netProfitParentCut_YOY():


    inter = interface.interFace('netProfitParentCut_YOY','2017-03-31',40.28,0.0641,-0.4798,-0.2568,3.1662,1.3747,-0.4490,1)
    print(inter.factor_interface())
    print(inter.ticket_pool())

    for i in range(0,7):
        if abs(inter.ticket_pool()[i]-inter.factor_interface()[i])<=0.09:
            pass
        else:
            print(i,'netProfitParentCut_YOY is error')

netProfitParentCut_YOY()