# HackerEarth.py

''' Question:
There are N friends of Jane. Jane is going to give some chocobars to them. The i'th friend should get atleast Ai chocobars. Jane asks them to line up.
Initially, the i-th friend stands at the i-th place of the line. Then Jane starts distribution of the chocobars. He follows the pattern as below:
    Give M chocobars to the first friend of the line.
    If this friend still haven't got enough chocobars, then the friend goes to the end of the line,else the friend goes home.
    Repeat the first two steps while the line is not empty.
Consider all the friends in the order they go home. Jane wants to know, which friend will be the last in this order?

INPUT FORMAT :
Line 1 contains N & M, the number of chocobars, and the number of chocobars given to each friend at a time.
Line 2 contains an array of N integers that denote the number of chocobars that each friend should atleast get.

OUTPUT FORMAT :
Output a single integer, representing the number of the last friend(here the number means the initial position).

CONSTRAINTS : 1 <= N <= 200
             1 <= Ai <= 200000 '''
             
# Program Code:

def lastfrnd(n,k,lst):
    maximum = 0
    for i in range(0,n):
        if(lst[i] <= k):continue    
        r =lst[i]//k
        if(r >= maximum):
            maximum = r
            ans = i+1
    if(maximum == 0):
        return(n)
    else:
        return(ans)

n,k = map(int,input().split())
lst = list(map(int,input().split()))
print(lastfrnd(n,k,lst))
