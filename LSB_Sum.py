# HackerEarth Problem

''' Question:
You are given an array of N integers, find the sum of all numbers whose Least Significant Bit in Binary representation is 0.

INPUT FORMAT:
Line 1 contains the number of test cases - T.
Line 2 - Each testcase contains a single integer N, followed by N integers denoting array elements.

OUTPUT FORMAT:
A single integer for each test case denoting the corresponding sum.'''

# Problem Code:

def lsbsum(lst):
    s=0
    for n in lst:
        if(n&1 == 1):continue
        s += n
    return(s)

t = int(input())
while(t):
    n = int(input())
    lst = list(map(int,input().split()))
    print(lsbsum(lst))
    t -= 1
