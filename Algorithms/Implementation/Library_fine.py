# library fine
# https://www.hackerrank.com/challenges/library-fine/problem?h_r=internal-search

import datetime

d1,m1,y1 = 9,6,2015 # returned date
d2,m2,y2 = 6,6,2015 # due date

fine = 0
# same month, year = 15 x (no.of days late)
# same year,diff month = 500 x (no.of months late)
# diff year = 10000

a = datetime.datetime(y1,m1,d1)
b = datetime.datetime(y2,m2,d2)
c = a-b

#print(a,b,a-b)
if y1 != y2:
    fine = 10000
elif m1 != m2 and y1 == y2:
    fine = 200 * abs(m1-m2)
elif d1 != d2 and m1 == m2 and y1== y2:
    fine = 15 * abs(d1-d2)

print(fine)