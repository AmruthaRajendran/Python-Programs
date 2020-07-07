# HackerRank Problem

# Question:Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 
# index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
# For example, if s=abc, it is a valid string because frequencies are 1. So is s=abcc because we can remove one c and have 1 of each character in the remaining string.
# If s=abccc however, the string is not valid as we can only remove 1 occurrence of c. That would leave character frequencies of {a:1,b:1,c:2}.

#Program Code:

import math
import os
import random
import re
import sys


def isValid(s):
    newstr = dict()
    count = 0
    indexes = list()
    for ch in s:
        newstr[ch] = newstr.get(ch,0)+1
    for ch,val in newstr.items():
        indexes.append(val)
    indexes = sorted(indexes,reverse=True)


    for i in range(0,len(indexes)-1):
        if(indexes[i] == indexes[i+1]):
            continue
        elif(i+1 == len(indexes)-1 and indexes[i+1]==1):
            count += 1
        elif( i!=0 and i+2 < len(indexes) and indexes[i+1]==indexes[i+2]):
            count += 3
        else:
            count += (indexes[i]-indexes[i+1])
    if(count <= 1):
        return("YES")
    else:
        return("NO")
    
# Main Program

s = input()
result = isValid(s)
print(result)
