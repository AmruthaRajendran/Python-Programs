# HACKERRANK PROBLEM

#John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock,
#determine how many pairs of socks with matching colors there are.For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. 
#There is one pair of color 1 and one of color . There are three odd socks left, one of each color. The number of pairs is 2.


#  Program Code:

import math
import os
import random
import re
import sys

# Here I created a new dictionary and for each sock color its count also updated.

def sockMerchant(n, ar):
    socks=dict()
    for sock in ar:
        socks[sock]=socks.get(sock,0)+1
    pairs=0
    for sock,count in socks.items():
        pairs=pairs+int(count/2)
    return(pairs)

# Here I used the same input output format of the hackerrank platform.
# We can use familiar format as to run on our editor


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
