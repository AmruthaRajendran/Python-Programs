# HackerEarth Problem

''' Question:
Xi Zhou loves programming contests!!!
Xi Zhou loves participating in programming contests. Once, he made a schedule of N upcoming contests. The schedule consists of the duration of those N contests.
However, Xi Zhou is a high school student and he has to prepare for his entrance exams, so he can only participate in contests that are having less duration.
He can skip no more than three consecutive contests. Find the minimum total duration of the contests, he can participate.

INPUT FORMAT:
Line 1 contains the number of test cases - N.
Line 2 - Contains N integers denoting the durations of N contests.

OUTPUT FORMAT:
A single integer denoting the minimum total duration of the contests he participated.    

CONSTRAINTS : 1 <= N <= 200000'''

# Program Code:

def minduration(lst,n):
    ans = 0
    i = 0
    l =n - n%3
    while(i<l):
        m = min(lst[i],lst[i+1],lst[i+2])
        ans += m
        i += 3
    if(n%3 == 0):
        return(ans)
    r = n%3
    if(r == 1):
        return(ans+lst[n-1])
    else:
        return(ans+min(lst[n-1],lst[n-2]))

n = int(input())
lst = list(map(int,input().split()))
print(minduration(lst,n))
