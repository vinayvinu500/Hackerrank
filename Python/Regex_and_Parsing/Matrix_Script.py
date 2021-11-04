# https://www.hackerrank.com/challenges/matrix-script/problem?h_r=internal-search

import re

#matrix size n x m
n,m = tuple(map(int,input().strip().split()))

#size allocation for letters
matrix = [[0]*m for _ in range(n)]

#rearranging letters in matrix
for i in range(n):
    line = input()
    for j in range(m):
        matrix[i][j] = line[j]
        
#matrix decoding
text = "".join((matrix[j][i] for i in range(m) for j in range(n))).strip()

#arranging letters in string
pattern = r'\w\W+\w'
rl = re.findall(pattern,text)
for i in rl:
    rl = re.findall(pattern,text)
    s=i[1:-1]
    text=text.replace(s, ' ',1)
print(text)

"""
7 3 
Tsi 
h%x 
i # 
sM 
$a 
#t% 
ir!

5 9 
#%$r%r$n 
O%Mi$iTi$ 
yiaxsprt 
est%ctiy# 
  t c i %
"""