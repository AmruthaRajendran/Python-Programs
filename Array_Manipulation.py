 # HackerRank problem

''' Question:Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in your array.
For example, the length of your array of zeros n=10 . Your list of queries is as follows:
    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of k between the indices a and b inclusive:
index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
  The largest value is 10 after all operations are performed.'''
  
  
 # PROGRAM CODE:
 # First approach:
  
import math
import os
import random
import re
import sys


def arrayManipulation(n, queries, m):
    ans = list()
    ans = [0]*n
    maximum = 0
    for i in range(0,m):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        for j in range(a-1,b):
            ans[j] += k
            if(ans[j] > maximum):
                maximum = ans[j]
    return(maximum)
    
# Here I used the logic of updating each cell of the array; in the range a:b; by adding the values of k with its previous value.

# I solved it in hackerrank so maintained the syntax and input output format of that platform.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries, m)
    fptr.write(str(result) + '\n')
    fptr.close()
    
    
    
          ''' "The above approach doesn't work for all the testcases in hackerrank because it is not efficient and take too much time and get into timeout.This is a brute force method"
           
           So I searched the discussion forum for an efficient program code and found this efficient and optimised code for the above problem.
           Reference: Hackerrank Disscussion Logic is well defined in the forum. 
           More detailed description for the logic Refer this you tube video: https://youtu.be/hDhf04AJIRs '''
           
  # Second Approach:
  # Here is the modified function:
   
   def arrayManipulation(n, queries):
    ans = list()
    ans = [0]*(n+1)
    maximum = 0
    result = 0
    a = queries[0]
    b = queries[1]
    k = queries[2]
    for a,b,k in queries:
        ans[a-1] += k
        ans[b] -= k
    for i in ans:
        result += i
        maximum = max(maximum,result) 
    return(maximum)
   
   
