# HackerEarth Problem

''' Question:
The Stellar Romance!
Too far in the future...
Humans have become a stellar civilization.

You have settled near a peaceful woods in the Mars. It was then, your better half was assigned on an official trip to the Earth.
Wanting to communicate with your partner, you are going to write an encryption program.

The process is as follows:
    - The program will accept a string as input.
    - The encrypted message will be output by the program.

The encryption will be as follows:
    - "HelloDear" will be encrypted as "H1e1l2o1D1e1a1r1"

Write the required program.

CONSTRAINTS:
    String Length <= 100000'''
    
# Program Code:

def Encryptmsg(msg):
    ans=""
    ch="0"
    for i in range(0,len(msg)-1):
        if(msg[i]==" "):continue                          # This command is to skip the blank space if exist.
        if(i+1 == len(msg)-1 and msg[i] != msg[i+1]):     # This line is to consider the final letter if it is not equal to the previous letter.
            ans += msg[i+1] + str(len(ch))
            break
        if(msg[i] == msg[i+1]):                           # Here we group the adjacent same letters together to track their count.
            ch += msg[i]
        else:
            ans += msg[i] + str(len(ch))
            ch = "0"                                      # After appending the letter and its corresponding count the ch is reinitialize with 0.
    return(ans)

lst = input()
print(Encryptmsg(lst))
