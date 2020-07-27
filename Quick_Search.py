# HackerEarth Problem

''' Question:
You are given two integer N, X, and N integers from A0, .., An-1.
You have to check whether X is present in those N integers.
If present print 1, else print 0. 
Note, the N elements are sorted.

INPUT FORMAT:
    The first line contains two integers N and X.
    The next line contains N integers, A0...An-1.

OUTPUT FORMAT:
    Print 1 if X exists, else print 0.

CONSTRAINTS:
     N <=100000
    |Ai|,|X|<=1000000'''

# Program Code:

n,x = map(int,input().split())
lst = map(int,input().split())
if x in lst:
    print(1)
else:
    print(0)
