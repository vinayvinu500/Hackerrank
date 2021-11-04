# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/30-review-loop/problem?h_r=internal-search

# user input
n = int(input())
arr = [input() for i in range(n)]
out = []
e = ''
o = ''
inp = ''
for i in arr:
    for ind, val in enumerate(i):
        if ind % 2 == 0:
            e += val
            pass
        else:
            o += val
            pass
    inp = e + ' ' + o
    out.append(inp)
    inp = ''
    e = ''
    o = ''
for j in out:
    print(j)
    pass

"""
Examples
2
Hacker
Rank
"""
