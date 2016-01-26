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

import random, string

orgs=[]
letters=string.printable #letters to choose from
target='''''' #the target string

num_orgs=10000
tolerance = num_orgs/2 #number of orgs to keep
mut_chance=10 #a one in x percent chance of mutation for each letter

def pop_orgs(pop_size): #Populate number of orgs
    for i in xrange(pop_size):
        new_org=""
        for x in xrange(len(target)):
            new_org=new_org + letters[random.randrange((len(letters)))]
        orgs.append(new_org)

def eval_org(org):
    score=len(target)
    for f in xrange(len(target)):
        if target[f]==org[f]:
            score-=1
    return score

def crossover_orgs(org1,org2):
    divider=random.randrange(len(target))
    return org1[:divider] + org2[divider:]

def s_repopulate_orgs(): #Sexual reproduction
    norgs = len(orgs)
    missing = num_orgs - norgs
    for r in xrange(missing):
        org1 = orgs[random.randrange(norgs)]
        org2 = orgs[random.randrange(norgs)]
        org_new = crossover_orgs(org1,org2)
        org_new = mutate_org(org_new)
        orgs.append(org_new)

def a_repopulate_orgs(): #Sexual reproduction
    norgs = len(orgs)
    missing = num_orgs - norgs
    for r in xrange(missing):
        org_new = orgs[random.randrange(norgs)]
        org_new = mutate_org(org_new)
        orgs.append(org_new)
        
def mutate_org(org):
    new=""
    for z in xrange(len(org)):
        s = random.randrange(mut_chance)
        if s == 1: #If there's a mutation
            new=new+letters[random.randrange(26)]
        else:
            new=new+org[z]
    return new

def filter_orgs():
    global orgs

    orgs.sort(key=eval_org)

    orgs=orgs[:tolerance]

def run(n):
    pop_orgs(num_orgs)
    if n == -1: #Run until completion
        best_org=""
        start=0
        while best_org != target:
            filter_orgs()
            print orgs[0]
            best_org=orgs[0]
            s_repopulate_orgs()
            print start
            start+=1
    else: #Run a specific amount of times
        for i in xrange(n): 
            filter_orgs()
            print orgs[0]
            s_repopulate_orgs()
            print i
    filter_orgs()

