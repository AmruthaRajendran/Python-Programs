# HackerEarth Problem

''' Question:
You are given an array of N positive integers.

The task is to check whether each number has only 3 factors. Each of these 3 factors must be prime.

INPUT FORMAT:
    The first line contains a single positive integer, N (1 ≤ N ≤ 100000), showing how many numbers are in the array.
    The next line contains N space-separated integers Ai (1 ≤ Ai  ≤ 1000000000000).

OUTPUT FORMAT:
    Print N lines: the i-th line should contain "YES" (without the quotes), if number Ai has only 3 factors and all 3 of them are prime, and "NO" (without the quotes), otherwise.
    Print in new line after every number.'''

# Program Code:

import math

def isPrime(n):
    count=0
    if(n==1 or n==2):
        return(1)
    for i in range(2,int(n/2)):
        if(count>1):
            return(0)
        else:
            if(n%i==0):
                count+=1
    return(1)

def TrippleFactor(n):
    root = math.sqrt(n)
    if(n==1):
        return(0)
    else:
        if int(root + 0.5)**2 == n:
            ans = isPrime(root)
            if(ans==1):
                return(1)
            else:
                return(0)
        else:
            return(0)

n = int(input())
lst = map(int,input().split())
crt = list()
for num in lst:
    if num in crt:
        print("YES")
    else:
        result = TrippleFactor(num)
        if(result == 1):
            crt.append(num)
            print("YES")
        else:
            print("NO")
