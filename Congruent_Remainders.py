# HackerEarth Problem

''' Question:
You are given two numbers N and K; K <= N.
You have to find the minimum non negative number that should be added to N to make it divisible by K.

INPUT FORMAT:
    The first line contains an integer T.
    The next T lines contains two integers N & K.

OUTPUT FORMAT:
    The T lines contains a single integer that should be added to N to make it divisible by K and should be non negative and minimum as possible.

CONSTRAINTS:
    1 <= T <= 10
    1 <= K <= N <= 100000 '''
    
# Program Code:

t = int(input())
for i in range(0,t):
    n,k = map(int,input().split())
    if(n%k == 0):
        print(0)
    else:
        print(k-n%k)
