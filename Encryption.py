# HackerRank Problem

''' Question:(https://www.hackerrank.com/challenges/encryption/problem)
Sample Input 0
haveaniceday
Sample Output 0
hae and via ecy
Explanation 0
L=12,sqrt(L) is between 3 and 4.
Rewritten with 3 rows and 4 columns:
have
anic
eday
Sample Input 1
feedthedog    
Sample Output 1
fto ehg ee dd
Explanation 1
L=10,sqrt(l)  is between 3 and 4.
Rewritten with 3 rows and 4 columns:
feed
thed
og '''

# Program Code:

import math

def encryption(s):
    r=math.floor(math.sqrt(len(s)))
    c=math.ceil(math.sqrt(len(s)))
    lst = ''
    for i in range(c):
        temp = ''
        for j in range(0,len(s),c):
            if(i+j>=len(s)):
                break
            temp += s[i+j]
        lst += temp + ' '
    return(lst)
        
if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)

