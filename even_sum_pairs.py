# HackerEarth Question
''' Question:
You are given an integer N and N integers from A0,..,An-1.
Calculate the number of pairs that will give an even sum.

INPUT FORMAT:
    The first line contains an integer N.
    The next line contains N integers, A0, ..., An-1.

OUTPUT FORMAT:
    Print the number of such possible pairs

CONSTRAINTS:
    N <= 30000
    Ai <=1000000'''

# Program code

def evensum(n,arr):
    ans = 0;
    for i in range(0,n):
        for j in range(i+1,n):
            if((arr[i]+arr[j])%2 == 0):
                ans+=1
    return(ans)

n = int(input())
arr = list(map(int,input().split()))
print(evensum(n,arr))
