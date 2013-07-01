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

if  len(sys.argv) != 3 : 
    print sys.argv[0] + " <file> <length>"
    exit(1)

tree = Phylo.read(sys.argv[1], "newick")

chars=['A', 'C', 'T', 'G', 'N']
taxa  = tree.get_terminals()

aln={}
for t in taxa : 
    aln[t] = ''


clades = tree.find_clades()
for c in clades:
    ts = c.get_terminals()
    print ",".join(map(lambda x : str(x)  , ts))



for i in xrange(1,int(sys.argv[2])): 
    charsHere = [ choice(chars) ] 

    numMut = 0
    while numMut == 0: 
        numMut = int(expovariate(1)) 
        
    clades = []
    for i in range(0,numMut): 
        clades.append(choice(tree.find_clades()).get_terminals() ) 
    
    for t in taxa: 
        aln[t] += charsHere[0]



print str(len(taxa)) + "\t" +  sys.argv[2]
for t in taxa:
    print str(t) + '\t' + aln[t]

