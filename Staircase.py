# HackerRank Problem

'''Question:
Consider a staircase of size n=4:

   #
  ##
 ###
####
Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.
Function Description
Complete the staircase function in the editor below. It should print a staircase as described above.
staircase has the following parameter(s):
n: an integer
Input Format
A single integer, n, denoting the size of the staircase.
Output Format
Print a staircase of size  using # symbols and spaces.
Note: The last line must have 0 spaces in it.
Sample Input
6 
Sample Output
     #
    ##
   ###
  ####
 #####
######
Explanation
The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n=6.'''

# Program Code

def staircase(n):
    ans = ''
    for i in range(1,n+1):
        ans += '#'
        print((n-i)*' ' + ans)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
