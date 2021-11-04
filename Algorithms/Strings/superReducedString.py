# https://www.hackerrank.com/challenges/reduced-string/problem?h_r=internal-search
s = 'aab'
s = 'abba'
# s = 'aaabccddd'

s = list(s)
d = []
# for_loop implementation
# for i in range(len(s) - 1):
#     a = s[i:i + 2]
#     print(a, (s[i], s[i + 1]))
    # if s[i] == s[i + 1]:
    #     d.append(s.pop(0))

# implementation of foreach
# for i in s:
#     ind = s.index(i)
#     print(ind, ind+1)
#     if s[ind] == s[ind+1]:
#         s.pop(ind)

# while implementation
print(s)
i = 0
while i < len(s)-1:
    print(s[i], s[i+1])
    if s[i] != s[i+1]:
        d.append(s.pop(i))
    i += 1

print(d)