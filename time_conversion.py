"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


def timeConversion(s):
    num = int(s[0:2])
    if (s[8:] == 'PM' and num != 12):
        conv = int(num) + 12
        return str(conv) + s[2:8]
    elif (num <= 12 and s[8:] == 'AM'):
        if(num == 12):
            conv = 12 - num
            return '0'+str(conv) + s[2:8]
        else:
            return s[:8] 
    elif (num == 12 and s[8:] == 'PM'):
        return s[:8] 

print(timeConversion('04:59:59AM')) 