# https://www.hackerrank.com/challenges/string-construction/problem?h_r=internal-search
# s = 'abcabc'
# s = 'abcd'
s = 'abc'
p = ''
n = len(s)
# append each letter to p and charge 1 dollar
# if s substring is in the p then simply append to p

substring = sorted(list(set(list(set(s)) + [s[:i] for i in range(1,n)] + [s])))
print(substring)

for i in range(n):
    p += s[i]
    print(i, p)
print(p)
