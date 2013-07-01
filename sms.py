#! /usr/bin/python 

# it turns out, it is faster to write your own inaccurate alignment
# simulator compared to an attempt to get indelible to run under
# recent linux version.

# the sequences produced here are not strongly biologically meaningful
# and mostly serve the purpose of having something to run your program
# on

from random import * 
from Bio import Phylo
import sys 


expNumberOfMutations = 3 

if  len(sys.argv) != 3 : 
    print sys.argv[0] + " <file> <length>"
    exit(1)

tree = Phylo.read(sys.argv[1], "newick")

chars=['A', 'C', 'T', 'G']
extChars=['A', 'C', 'T', 'G', 'N']

taxa  = tree.get_terminals()

aln={}
for t in taxa : 
    aln[t] = []


clades = tree.find_clades()
for c in clades:
    ts = c.get_terminals()
    # print ",".join(map(lambda x : str(x)  , ts))


for i in xrange(0,int(sys.argv[2])): 
    char =  choice(chars)

    numMut = 0
    while numMut == 0: 
        numMut = int(expovariate(expNumberOfMutations)) 
        
    clades = []
    for j in range(0,numMut) : 
        clade = choice(list(tree.find_clades()))        
        clades.append(clade) 

    lenList = map( lambda x : len(x.get_terminals()), clades )
    orderList = sorted(range(len(lenList)),key=lambda x:lenList[x], reverse=True )
    orderedClades =  [ clades[j] for j in orderList ] 

    for t in taxa: 
        aln[t].append(char) 

    for c in orderedClades:
        ts = c.get_terminals()
        
        curChar = aln[ts[0]][i]
        newChar = curChar
        while curChar == newChar: 
            curChar = choice(extChars)

        for t in ts:
            aln[t][i] = curChar

    # print "iter " + str(i) 


print str(len(taxa)) + "\t" +  sys.argv[2]
for t in taxa:
    print str(t) + '\t' + "".join(aln[t])

