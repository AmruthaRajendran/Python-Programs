# HackerEarth Problem

''' Question:Subha is a brilliant ethical hacker.
Once she was assigned to break into a hidden network, as part of an investigation by the state.
The network had an integer password.
With her observation skills, Subha understood how to obtain the password.

As she is a busy woman, she asked you to take the case and gave you instructions to figure out the password.

Subha's instructions were:
        The random words displayed by the system are not random.
        The password is the number of unique string lengths in the displayed words.

INPUT FORMAT:
    The first line contains the number of strings - N
    Next N lines contain a single string each.

    All letters are in lowercase.'''
    
# Solution:

def uniquepassword(lst):
    wordlength = dict()
    for word in lst:
        wordlength[len(word)] = wordlength.get(len(word),0)+1
    return(len(wordlength))

lst = list()
n = int(input())
for i in range(0,n):
    lst.append(input())
print(uniquepassword(lst))
