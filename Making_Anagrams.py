# HackerRank Problem

# Question: Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters 
# can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are 
# anagrams, but bacdc and dcbad are not.

# Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings 
# anagrams. Can you help her find this number?

# Input Format:
# The first line contains a single string,a .
# The second line contains a single string,b .

# Output Format:
# Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

# Program Code:

import math
import os
import random
import re
import sys

# Here first we create a dictionary to store the number of occurences of each character in the two strings
# Then we count the number of characters which are common in both strings
# Then substract the count*2 from the total length of two strings.

def makeAnagram(a, b):
    ans = 0
    str1 = dict()
    str2 = dict()
    for ch in a:
        str1[ch] = str1.get(ch,0) + 1
    for ch in b:
        str2[ch] = str2.get(ch,0) + 1
    
    for ch,count in str1.items():
        if(ch in str2):
            ans += min(count,str2[ch])        # some characters may occur different number of times in strings so we have to count the minimum occurences. 

    result = len(a) + len(b) - (2*ans)

    return(result)


a = input()
b = input()
res = makeAnagram(a, b)
print(res)
