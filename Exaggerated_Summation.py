# HackerEarth Problem

''' Question:
The Exaggerated Summation
Gwen gives Ben N integers in binary form and asks him to find whether their sum is even or odd.
    It's pretty easy right, but Gwen gives Ben a large number of such numbers, help Ben, find whether their sum is even or odd.

INPUT FORMAT:    
    The first line contains N numbers.
    The following N lines contain binary representation of numbers.

OUTPUT FORMAT:
    You have to print "EVEN", if their sum is even (in decimal) or print "ODD", if its odd.
    Constraints : 1 <= N <=1000'''
    
# Program Code:

def evenorodd(lst):
    count=0;
    for num in lst:
        if(num[len(num)-1] == '1'):
            count += 1;
    if(count%2 == 1):
        print("ODD")
    else:
        print("EVEN")

lst = list()
n = int(input())
for i in range(0,n):
    lst.append(input())
evenorodd(lst)
