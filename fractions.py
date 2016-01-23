#   Copyright (C) 2016 Jacob Bender and Christopher King

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random, math

orcs = [(1.0,1.0)]
numOfOrcs = 1000
tolerance = 500
mutateiters = 100
target=math.pi

def eval_orc(orc):
    try:
        out=orc[0]/orc[1]
        score=abs(target-out)
    except(ZeroDivisionError):
        score=9001 #It's over 9000
    return score

def filter_orcs():
    global orcs

    orcs.sort(key=eval_orc)

    orcs=orcs[:tolerance]
    
def mutate_orc(orc):
    x=random.randrange(5)
    num = orc[0]
    den = orc[1]
    if x == 0:
        return orc
    elif x==1:
        return (num+1,den)
    elif x==2:
        return (num-1,den)
    elif x==3:
        return (num,den+1)
    elif x==4:
        return (num,den-1)

def crossover_orcs(orc1,orc2):
    return (orc1[0],orc2[1])

def repopulate_orcs():
    norcs = len(orcs)
    missing = numOfOrcs - norcs
    for i in xrange(missing):
        orc1 = orcs[random.randrange(norcs)]
        orc2 = orcs[random.randrange(norcs)]
        orc_new = crossover_orcs(orc1,orc2)
        for i in xrange(mutateiters):
            orc_new = mutate_orc(orc_new)
        orcs.append(orc_new)

def run(n):
    for i in xrange(n):
        repopulate_orcs()
        filter_orcs()
        print i
    print orcs
