# HackerEarth Problem

''' Question:
You will be given a word as input.
If all letters of the word are different, output "YES" else output "NO" (Without double quotes).

INPUT FORMAT:
    The input contains a single string.
    Note: all letters are of the string are in lowercase.'''
    
# Solution:

def distinctword(str):
    lst = dict()
    for ch in str:
        lst[ch] = lst.get(ch,0)+1          # To check if the word consists of unique letters, a dictionary of characters in the word is created.
                                           # Then the count of each character is checked whether they are occuring more than once or not.
    for ch,count in lst.items():
        if(count>1):
            return("NO")
    return("YES")

word = input()
print(distinctword(word))
