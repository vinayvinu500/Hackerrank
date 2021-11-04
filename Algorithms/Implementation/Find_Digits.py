# divisor 
# https://www.hackerrank.com/challenges/find-digits/problem?h_r=internal-search

n = 1012
temp = n
c = 0

while n:
    i = n%10
    n //= 10
    if i != 0 and temp%i==0:
        print(i,n,temp,temp%i)
        c += 1

print(c)