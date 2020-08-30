# HackerEarth Problem (PTIB Coding Test)

'''Question:
GOAL!
It's ISL time and as usual Kerala Blasters FC is finding it tough to qualify for playoffs, but they want to settle the debts of the last season.
KBFC needs a minimum of X more points to qualify for playoffs in their remaining Y matches. A win, a draw and a loss in a match will yield 2, 1, 0 points respectively to a team.

You are a die hard KBFC fan and want to find the minimum number of matches KBFC needs to win to qualify for play offs.
It is guaranteed that KBFC will qualify for playoffs if they win all their remaining Y matches.

Calculate the minimum number of games KBFC needs to win, so that they can start settling the previous season's debt.

INPUT FORMAT:
    Line 1 contains the number of test cases - T
    Line 2 - T+1 contains 2 space separated integers (X Y) each

OUTPUT FORMAT:
    A single integer denoting the minimum number of WINS required for the team to qualify. '''
    
# Program:

def matchesreq(x,y):
    if(x<=y):
        return(0)
    if(x//2 >= y):
        if(x%2 == 1):
            return(0)
        return(x//2)
    return(x-y)

t = int(input())
while(t!=0):
    x,y = map(int,input().split())
    print(matchesreq(x,y))
    t -= 1
