from collections import defaultdict
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?h_r=internal-search

d = defaultdict(list)

d['A'].extend(['a','a','b','a','b'])

d['B'].extend(['a','b'])

print(d)

for x in d['B']:
	if x in d['A']:
		for i,j in enumerate(d['A'],start=1):
			if x == j:
				print(i,end=' ')
		print()
	else:
		print(-1)