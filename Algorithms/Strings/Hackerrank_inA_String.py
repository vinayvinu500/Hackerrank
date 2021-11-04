# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?h_r=internal-search

w = 'hackerrank'
s = 'haacckkerrannkk'
s = 'haacckkerannk'
s = 'hccaakkerrannkk'
s = 'hereiamstackerrank'
s = 'hackerworld'
s = 'hhaacckkekraraannk'
s = 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'
n = len(s)
r = ''
w = list(w)


print(w)
print(s)

for i in range(n):
    #print(w[0],s[i],r)
    if len(w) == 0:
        break
    if w[0] == s[i]:
        r += w.pop(0)
print(r)
r = 'YES' if r == 'hackerrank' else 'NO'
print(r)