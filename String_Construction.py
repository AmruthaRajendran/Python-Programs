# HackerRank Problem

''' Question:
Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following operations with the given costs. She can perform them any number of
times to construct a new string p:

Append a character to the end of string p at a cost of 1$ dollar.
Choose any substring of p and append it to the end of p at no charge.
Given n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

For example, given a string s=abcabc, it can be copied for 3 dollars. Start by copying a, b and c individually at a cost of 1 dollar per character. String p=abc at this time. Copy 
p=[0:2] to the end of p at no cost to complete the copy.

Function Description

Complete the stringConstruction function in the editor below. It should return the minimum cost of copying a string.

stringConstruction has the following parameter(s):

s: a string
Input Format

The first line contains a single integer n, the number of strings.
Each of the next n lines contains a single string, s[i].

Output Format

For each string s[i] print the minimum cost of constructing a new string p[i] on a new line.

Sample Input

2
abcd
abab
Sample Output

4
2
Explanation

Query 0: We start with s="abcd" and p="".

Append character 'a' to p at a cost of 1 dollar, p="a".
Append character 'b' to p at a cost of 1 dollar, p="ab".
Append character 'c' to p at a cost of 1 dollar, p="abc".
Append character 'd' to p at a cost of 1 dollar, p="abcd".
Because the total cost of all operations is 4 dollars, we print 4 on a new line.

Query 1: We start with s="abab" and p="".

Append character 'a' to p at a cost of 1 dollar, p="a".
Append character 'b' to p at a cost of 1 dollar, p="b".
Append substring "ab" to p at no cost, p="abab".
Because the total cost of all operations is 2 dollars, we print 2 on a new line.

Note
A substring of a string S is another string S' that occurs "in" S. For example, the substrings of the string "abc" are "a", "b" ,"c", "ab", "bc", and "abc".'''

# Program Code:

def stringConstruction(s):
    p = ''
    amt = 0
    for ch in s:
        if ch in p:continue
        p += ch
        amt += 1
    return(amt)

q = int(input())
for i in range(q):
    s = input()
    result = stringConstruction(s)
    print(result)
