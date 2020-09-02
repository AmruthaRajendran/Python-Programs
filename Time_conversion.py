# Hackerrank Problem

''' Question:
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter(s):
s: a string representing time in 12 hour format.

Sample Input 0
07:05:45PM
Sample Output 0
19:05:45 '''

# Progam Code:

def timeConversion(s):
    ans = int(s[:2])+12
    if(ans==24):
        if(s[8:]=='AM'):
            return('00'+s[2:8])
        else:
            return(s[:8])
    if(s[8:] == 'AM'):
        return(s[:8])
    return(str(ans)+s[2:8])

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
