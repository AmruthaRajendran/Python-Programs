# HackerRank Problem

''' Question:Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array arr=[-2,2,4]
we can create 3 pairs of numbers:[-2,2],[-2,4] and [2,4]. The absolute differences for these pairs are 4,6 and 2. The minimum absolute difference is 2.'''

# Program Code:



# Here first we sort the given array. Then for adjacent elements absolute difference is calculated and find the minimum difference.
# The array is sorted so that we need only one traversal across the entire array to find the minimum difference.

def minimumAbsoluteDifference(arr):
    newarray = sorted(arr)
    diff = 0
    minimum = abs(newarray[0]-newarray[1])
    for i in range(0,len(newarray)-1):
        diff = abs(newarray[i] - newarray[i+1])
        if(diff < minimum):
            minimum = diff       
    return(minimum)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
