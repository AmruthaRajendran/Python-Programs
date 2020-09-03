# Hackerrank Problem

''' Question:
A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers,
you have the same value you started with.
In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add
up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.
Input Format
The first line contains the lower integer limit p.
The second line contains the upper integer limit q.
Note: Your range should be inclusive of the limits.
Output Format
Output each modified Kaprekar number in the given range, space-separated on a single line. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE.
Sample Input
1
100
Sample Output
1 9 45 55 99. '''

# Program Code:

def kaprekarNumbers(p, q):
    lst = list()
    for i in range(p,q+1):
        s = str(i*i);
        l = len(s)
        if(i == 1):
            print(i,end=" ")
        if(l == 1):continue
        t1 = int(s[0:l//2])
        t2 = int(s[l//2:])
        if(t1+t2 == i):
            lst.append(i)
            print(i,end=" ")
    if(len(lst) == 0):
        print("INVALID RANGE")
    
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
