# HackerEarth Problem

''' Question:
Gennady is given a task. The task is as follows, he is given N stones which could be of colors Green, Red, or Blue. He is asked to find the minimum
number of stones to be removed from those N stones such that no two adjacent stones will have the same colour. Help Gennady, find the answer.

INPUT FORMAT:
    Line 1 contains N, the number of stones.
    Line 2 contains a string of N letters, where each letter corresponds to its mentioned colour in      the question.

OUTPUT FORMAT:
    A single integer denoting the minimum number of coins to be removed for the condition         mentioned in the question.

CONSTRAINTS: 1 <= N <= 60.'''

# Program Code:

def minremoval(n,arr):
    count = 0
    for i in range(0,n-1):
        if(arr[i] == arr[i+1]):
            count += 1
    return(count)

n = int(input())
s = input()
print(minremoval(n,s))
