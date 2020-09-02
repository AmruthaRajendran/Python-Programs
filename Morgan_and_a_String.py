# HackerRank Problem
''' Question:
Jack and Daniel are friends. Both of them like letters, especially upper-case ones.
They are cutting upper-case letters from newspapers, and each one of them has his collection of letters stored in a stack.
One beautiful day, Morgan visited Jack and Daniel. He saw their collections. He wondered what is the lexicographically minimal string made of those two collections.
He can take a letter from a collection only when it is on the top of the stack. Morgan wants to use all of the letters in their collections.

As an example, assume Jack has collected a=[A,C,A] and Daniel has b=[B,C,F]. The example shows the top at index 0 for each stack of letters.
Assembling the string would go as follows:
Jack	Daniel	result
ACA	  BCF
CA	  BCF	    A
CA	  CF	    AB
A	  CF	    ABC
A 	  CF	    ABCA
         F	    ABCAC
    		    ABCACF
Note the choice when there was a tie at CA and CF.

Function Description
Complete the morganAndString function in the editor below. It should return the completed string.
morganAndString has the following parameter(s):
a: a string representing Jack's letters, top at index 0.
b: a string representing Daniel's letters, top at index 0.
Input Format

The first line contains the an integer t, the number of test cases.

The next t pairs of lines are as follows:
- The first line contains string a.
- The second line contains string b.

Output Format:
Output the lexicographically minimal string  for each test case in new line.

Sample Input:

2
JACK
DANIEL
ABACABA
ABACABA
Sample Output

DAJACKNIEL
AABABACABACABA

Explanation:
The first letters to choose from were J and D since they were at the top of the stack. D was chosen, the options then were J and A. A chosen. 
Then the two stacks have J and N, so J is chosen. (Current string is DAJ) Continuing this way till the end gives us the resulting string.'''

# Program Code:

def morganAndString(a, b):
    i = 0
    s = ''
    a += 'z'
    b += 'z'
    l = len(a) + len(b)
    while(i!=l-2):
        if(len(a) == 0):
            s += b[0:]
            break
        if(len(b) == 0):
            s += a[0:]
            break
        if(a<b):
            s += a[0]
            a = a[1:]    
        else:
            s += b[0]
            b = b[1:]
        i += 1
    return(s)



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        result = morganAndString(a,b)
        print(result)
