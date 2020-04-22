import sys
from random import *

# This program can be run with the test input inp1.txt
# To run this program use command 'python3 process.py < inp1.txt'

line = sys.stdin.readline() 
linecount = 1
while line:
    #Check if its the 10th line
    if (linecount % 10 == 0) :
        print(line)
    
    #Generate random number between 0 to 1
    check = random()
    if (check >= 0.5):
        print(line, file=sys.stderr)

    #move to next line and increment line counter
    line = sys.stdin.readline()
    linecount += 1

