# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?h_r=profile

# strings palindrome
s = 'cde'
#s = 'abc'
s = 'abcba'
s = 'abcd'
s = 'cba'

print(s)
#s = list(map(ord,s))
n = len(s)
l = n//2
r = 0
# len of string = n
# last element = first element
# s[-1] = s[0]
print(s)
print('n = ',n,'\nl = ',l)
print()
for o in range(l):
    ind = n-(o+1)
    print(o,ind,s[ind],s[o])
    if s[ind] != s[o]:
        print(ord(s[ind])-ord(s[o]))
        r += abs(ord(s[ind])-ord(s[o]))
    print(r)