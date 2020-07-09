# HackerRank Problem
'''Question:Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know 
if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words 
available in the magazine. He cannot use substrings or concatenation to create the words he needs.
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is No.'''

#Program Code:

import math
import os
import random
import re
import sys

# Here we first convert the two sentences into dictionaries. Then check whether each word in note is in magazine.

def checkMagazine(magazine, note):
    Magazinewords = dict()
    Notewords = dict()
    ans = 0
    for word in magazine:
        Magazinewords[word] = Magazinewords.get(word,0)+1
    for word in note:
        Notewords[word] = Notewords.get(word,0)+1
    for word,count in Notewords.items():
        if word in Magazinewords:
            if(Magazinewords.get(word) >= count):
                ans += 1
    if(ans == len(Notewords)):
        print("Yes")
    else:
        print("No")

        
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
