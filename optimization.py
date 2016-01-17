import random, math

orcs = [(1,1)]

def eval_orc(orc):
    try:
        out=orc[0]/orc[1]
        score=abs(math.pi-out)
    except(ZeroDivisionError):
        score=9001 #It's over 9000
    return score
    
