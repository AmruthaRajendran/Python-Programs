# HackerEarth Problem

'''Question:
You are given a an integer N, X, and N integers from A0, .., An-1.
You have to check whether there is a number in those N integers such that sum of X and that number is 0.

INPUT FORMAT:
    The first line contains an integer T.
    Next T lines follow the format below:
    N X
    A0, ....., An-1

OUTPUT FORMAT:
    T Lines contains either YES or NO, according to whether such an integer is found in array or not.

CONSTRAINTS:
    T <=100
    N <=100000
    |Ai|,|X|<=1000000 '''
    
# Program Code:

t = int(input())
for i in range(0,t):
    n,num=map(int,input().split())
    lst = map(int,input().split())
    if num*-1 in lst:                    # We get zero on adding two numbers only when the numbers are complement of each other. so we need to check whether negative of the number
        print("YES")                     # is there in the lst or not.
    else:
        print("NO")
