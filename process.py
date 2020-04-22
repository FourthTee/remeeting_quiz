import sys
from random import *

line = sys.stdin.readline() 
linecount = 1
while line:
    if (linecount % 10 == 0) :
        print(line)
    check = random()
    if (check >= 0.5):
        print(line, file=sys.stderr)
    line = sys.stdin.readline()
    linecount += 1

