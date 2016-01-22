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
tolerance = 5 #number of orgs to keep
letters=string.lowercase #letters to choose from
target="abc" #the target string

def pop_orgs(pop_size): #Populate number of orgs
    for i in xrange(pop_size):
        new_org=""
        for x in xrange(len(target)):
            new_org=new_org + letters[random.randrange(26)]
        orgs.append(new_org)

def eval_org(org):
    score=len(target)
    for x in xrange(len(target)):
        if target[x]==org[x]:
            score-=1
    return score

def filter_orgs():
    global orgs
    
    orgs.sort(key=eval_org)

    orgs=orgs[:tolerance]                

