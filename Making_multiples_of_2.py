# Hackerearth Problem

''' Question:
Barney and Mosby are close friends. One day, Barney gave Mosby, a number Z. He then asked Mosby to multiply Z by 2 as many times until the Z becomes divisible by 10.
Since you are his close friend, help Mosby find the minimum moves (can also be 0) required to satisfy the condition mentioned above.

INPUT FORMAT : Line 1 - contains an integer T denoting the number of testcases.
              Next T lines contain a single integer Z.

OUTPUT FORMAT : For each Testcase, print the minimum number of moves.

CONSTRAINTS : 1 <= T <= 1000, 1 <= X <= 1000000000

Sample:
Input:
5
555
234
100
456
43
Output:
1
-1
0
-1
-1 '''

# Program Code:

def minmove(z):
    if(z%5 == 0 and z%10 != 0):
        return(1)
    elif(z%10 == 0):
        return(0)
    else:
        return(-1)

t = int(input())
while(t):
    z = int(input())
    print(minmove(z))
    t -= 1

