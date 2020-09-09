# HackerRank Problem

[Question](https://www.hackerrank.com/challenges/encryption/problem)

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

