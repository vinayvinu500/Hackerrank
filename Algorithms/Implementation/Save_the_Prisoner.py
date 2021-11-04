# https://www.hackerrank.com/challenges/save-the-prisoner/problem?h_r=internal-search
# no of prisoner
n = 3
# no of candies
m = 7
# starting index
s = 3


# candies / n => remaining candies to distribute from index 0 and s -1 is add to remainder

print(m%n+(s-1))
c = m % n
k = (c+s-1) %n
if k == 0:
    print(n)
else:    
    print(k)

arr = []
i = s -1

print('n =\t',n)
print('m =\t',m)
print('s =\t',s)
print('i =\t',i)
print('value = ',list(range(1,n+1)))
print('index = ',list(range(n)))

while True:
    if i == m+s:
        break
    arr.append(range(n)[i%n]+1)
    i += 1

print('candy = ',arr)
print('result = ',arr[-1])

print(list(range(s,m+s)),end='\n\n')
a = [range(n)[(i-1)%n]+1 for i in range(s,m+s)]
print(a)
