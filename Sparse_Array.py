# HackerRank Problem

# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
# For example, given input strings=['ab','ab','abc'] and queries=['ab','abc','bc'], we find 2 instances of 'ab',1 of 'abc' and 0 of 'bc'. For each query,
# we add an element to our return array,results=[2,1,0].


# Program Code

import math
import os
import random
import re
import sys

# Here i made an empty dictionary and added the items of strings and updated each string's count. Then compared with the strings in queries.
def matchingStrings(strings, queries):
    ans = list()
    counts = dict()
    for word in strings:
        counts[word] = counts.get(word,0)+1
    for word in queries:
        if word in counts:
            ans.append(counts[word])
        else:
            ans.append("0")
        
    return(ans)
   
   
   # The input and output syntax is same as given in HackerRank we can switch to other input and output formats.
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
