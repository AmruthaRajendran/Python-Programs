# HackerRank Problem

''' Question:
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a 
cost associated with it.
Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire 
pool of money during each visit. ID numbers are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types of ice cream that
Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

For example, there are n=5 flavors having cost=[2,1,3,5,6]. Together they have money=5 to spend. They would purchase flavor ID's 1 and 3 for a cost of 2+3=5. Use 1 based indexing
for your response.'''

# Program Code

def whatFlavors(cost, money):
    temp = {}
    for index,firstone in enumerate(cost):
        secondone = money - firstone
        if secondone in temp.keys():
            print(temp[secondone]+1,index+1)
            break
        else:
            temp[firstone] = index
            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
