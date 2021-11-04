# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen

def timeConversion(s):
     m = s[-2:]
    x = s[:2]
    if x == '12' and m == 'AM':
        return '00'+s[2:-2]
    if x == '12' and m == 'PM':
        return s[:-2]
    if m == 'AM':
        return s[:-2]
    if m == 'PM':
        x = int(x) + 12
        return str(x)+s[2:-2]



# AM-PM
s = '12:05:45AM'
s = '12:05:45PM'


# PM conversion
s = '07:05:45AM'
s = '07:05:45PM'
timeConversion(s)



"""
https://www.freecodecamp.org/news/mathematics-converting-am-pm-to-24-hour-clock/

12:00 AM = 00:00
12:00 PM = 12:00

AM -> 1-11 == 1-11
PM -> 1-11 = 13-23
"""