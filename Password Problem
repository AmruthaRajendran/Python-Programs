# This was asked on the SAP Labs online preplacement test.
# Question: you are given two strings from which you have to create a new string which is considered as a password.
# The password should be made by combining the letters from each string in alternate fashion.
# eg: input: abc, def output: adbecf

#Program:

def FindPassword(a,b):
    n1 = len(a)
    n2 = len(b)
    n = n1 + n2
    newpassword = ' '
    l = 0
    k = 0
    for i in range(0,n):
        if(n1 == n2):                                # For equal length strings we can directly append alternatively.
            if(i%2 == 0):                            # The first string letters will be in positions 0,2,4,etc that is on even number positions.
                newpassword += a[l]
                l += 1
            else:
                newpassword += b[k]
                k += 1
        elif(n1 > n2):                               # For different lengths remaining length is filled with the largest strings remaining letters.
            if(i%2 == 1 and k < n2):                 # The second string letters will be in odd numbered positions.
                newpassword += b[k]
                k += 1
            else:
                newpassword += a[l]
                l += 1
        elif(n2 > n1):
            if(i%2 == 0 and l < n1):
                newpassword += a[l]
                l += 1
            else:
                newpassword += b[k]
                k += 1
    return(newpassword)
# main program
a = input()
b = input()
ans = FindPassword(a,b)
print(ans)
