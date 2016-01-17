import random

orcs = [(1,1)]

def mutate(orc):
    x=random.randrange(5)
    num = orc[0]
    den = orc[1]
    if x == 0:
        return orc
    elif x==1:
        return (orc[0]+1,orc[1])
    elif x==2:
        return (orc[0]-1,orc[1])
    elif x==3:
        return (orc[0],orc[1]+1)
    elif x==4:
        return (orc[0],orc[1]-1)
