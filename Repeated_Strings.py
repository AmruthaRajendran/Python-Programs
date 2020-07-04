# HackerRank Problem

# Question:Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.For example, if the string s='abcac' and n=10,
# the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

# Program code:

import math
import os
import random
import re
import sys

# Here we first count the number of 'a' in the given string. And calculate how many times the whole string repeats when it is extended to infinite length.
# Hence 'a' repeats that much times in the infinite string. The we count the number of 'a' in the remaining length of the infinite string. And add it to the count.

def repeatedString(s, n):
    if(s=='a' and len(s)==1):     # if 'a' is the only element in the string the number of 'a' is the the length of the infinite string.
        return(n)                   
    totallength = len(s)
    rep = int(n/totallength)
    count=0
    for ch in s:
        if(ch=='a'):
            count+=1
    if(count==0):
        return(0)
    remaininglen = n % totallength
    count = count*rep
    for i in range(0,remaininglen):
        if(s[i]=='a'):
            count+=1
    return(count)
    

s = input()
n = int(input())
result = repeatedString(s, n)
print(result)
