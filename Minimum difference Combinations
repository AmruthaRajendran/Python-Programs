# Question taken from the SAP Labs online placement test conducted.


# Question: You are given an array of length n.
# You have to find the minimum difference among the numbers in the array.
# And also to print that combinations which gives the minimum difference

def ComboOfmindiff(a,n):
    diff = 0
    minimum = 0
    # First we find the minimum difference among all the possible combinations
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i] == a[j]):continue
            diff = abs(a[i] - a[j])
            if(i == 0):
                minimum = diff
            elif(diff < minimum):
                minimum = diff
    # Then we print the combinations
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i] == a[j]):continue
            if(abs(a[i]-a[j]) == minimum):
                print(a[i]," ",a[j])

n = int(input("Length of array:"))
a = list(map(int,input().strip().split()))
ComboOfmindiff(a,n)
