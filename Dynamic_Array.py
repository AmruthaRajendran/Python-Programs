# HackerRank Problem

''' Question: 
Create a list, sequencelist, of N empty sequences, where each sequence is indexed from 0 to N. The elements within each of the  sequences also use 0-indexing.
Create an integer, lastanswer, and initialize it to 0.
The  types of queries that can be performed on your list of sequences (sequencelist) are described below:
Query: 1 x y
Find the sequence, sequence, at index  ((x XOR lastanswer)%N) in sequencelist.
Append integer y to sequence .
Query: 2 x y
Find the sequence, sequence, at index ((x XOR lastanswer)%N) in sequencelist.
Find the value of element y%size in sequence (where size is the size of sequence) and assign it to lastanswer.
Print the new value of lastanswer on a new line.
Task
Given N, Q, and Q queries, execute each query.

Note:XOR is ^ operator in most languages. Learn more about it on Wikipedia.

Input Format

The first line contains two space-separated integers, N(the number of sequences) and Q (the number of queries), respectively.
Each of the Q subsequent lines contains a query in the format defined above.

Output Format

For each type 2 query, print the updated value of lastanswer on a new line.'''

# Program Code:

def dynamicArray(n, queries):
    seq = [[] for i in range(n)]
    q =len(queries)
    lastans = 0
    result = list()
    for i in range(0,q):
        a =queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        if(a == 1):
            seq[(x^lastans)%n].append(y)
        elif(a == 2):
            temp = seq[(x^lastans)%n]
            val = temp[y%len(temp)]
            result.append(val)
            lastans = val
    return(result)
     
if __name__ == '__main__':

    n,q = map(int,input().split())

    queries = list()

    for i in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    for i in range(0,len(result)):
        print(result[i])

