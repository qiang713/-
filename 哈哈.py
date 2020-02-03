from sys import argv
from os.path import exists
A, B, C, = argv
D = open(B)
ceshi = D.read()
E = open(C,'w')
E.write(ceshi)
D.close()
E.close()
