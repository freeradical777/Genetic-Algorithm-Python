#   Copyright (C) 2016 Jacob Bender

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
tolerance = 500 #number of orgs to keep
letters=string.lowercase #letters to choose from
target="abc" #the target string

def pop_orgs(pop_size): #Populate number of orgs
    for i in xrange(pop_size)
        new_org=""
        for x in xrange(len(target)):
            new_org=new_org + random.choice(letters)
        orgs.append(new_org)

