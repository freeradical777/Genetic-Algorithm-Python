import random, math

orcs = [(1,1)]
numOfOrcs = 1000

def eval_orc(orc):
    try:
        out=orc[0]/orc[1]
        score=abs(math.pi-out)
    except(ZeroDivisionError):
        score=9001 #It's over 9000
    return score

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

def repopulate():
    norcs = len(orcs)
    missing = numOfOrcs - norcs
    for i in xrange(missing):
        orc = orcs[random.randrange(norcs)]
        orcs.append(mutate(orc))
