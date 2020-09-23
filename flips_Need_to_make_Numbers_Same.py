# Hackerearth Problem

''' Question:
DARK : DOPPLER AND NIELSEN
Doppler and Nielsen were solving a puzzle (as it is DARK), In the puzzle, they were given two numbers,  X and Y.
The puzzle asks them to find the number of moves such that you can convert X to Y. Each move is described as flipping a bit in X (in binary representation).
INPUT FORMAT : Line 1 - contains two numbers X, and Y.
OUTPUT FORMAT : The number of moves required to convert X to Y.
CONSTRAINTS :  1 <= X, Y <= 1000000000

Sample:
1.
Input:
4 6
Output:
1
2.
Input:
5 2
Output:
3 '''

# Program Code:

def flipsreq(n,m):
    flip = 0
    while(n!=0 or m!=0):
        temp1 = n & 1
        temp2 = m & 1
        if(temp1 | temp2 == 1 and temp1!=temp2):
            flip += 1
        n >>= 1
        m >>= 1
    return(flip)

n,m = map(int,input().split())
print(flipsreq(n,m))
