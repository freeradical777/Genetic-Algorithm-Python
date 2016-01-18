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

def filter_orcs():
    global orcs
    scores_list = []
    avg_score=0
    for orc in orcs:
        scores_list.append(eval_orc(orc))
    for score in scores_list:
        avg_score+=score

    avg_score=avg_score/len(scores_list)

    new_orcs=[]

    for x in xrange(len(orcs)):
        if scores_list[x] > avg_score:
            new_orcs.append(orcs[x])

    orcs=new_orcs
    
def mutate_orc(orc):
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

def repopulate_orcs():
    norcs = len(orcs)
    missing = numOfOrcs - norcs
    for i in xrange(missing):
        orc = orcs[random.randrange(norcs)]
        orcs.append(mutate_orc(orc))

def run(n):
    for i in xrange(n):
        print "Repopulating"
        repopulate_orcs()
        print "Killing bad orcs"
        filter_orcs()
        print "Orcs are ", orcs
