''' Question:
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass? '''

# Program Code:

def sumexists(lst,k):
    temp = dict()
    for index,item in enumerate(lst):
        d = k-item
        if d in temp:
            print(temp[d],index)
            return('True')
        else:
            temp[item] = temp.get(item,index)
    return('False')

lst = list(map(int,input().split()))
k = int(input())
print(sumexists(lst,k))
