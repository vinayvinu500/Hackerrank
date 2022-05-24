# https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true

import os, sys
import string
from collections import Counter as ct
# from itertools import combinations as cb,product as pd, permutations as pt


#========================================================dataSet=============================================================#
# print(os.getcwd())
# print(os.listdir())
with open('testCase_07.txt','r+') as f:
	si = ''.join(map(lambda x: x.replace('\n',''),f.readline()))
	q = [int(f.readline()) for i in range(int(f.readline()))]
	o = list(map(lambda x: x.replace('\n',''),f.readlines()))

#========================================================Algorithm=============================================================#
s = ['apple','hack','watch','ccccc','aaa','zzzz','xiamio','hackerrank','aaabbbbcccddd','appianipped','abbcccdddd']
s = 'abbcccdddd',[1,7,5,4,15]
# s = 'abcddde',[1,3,12,5,9,10]


# contigous character counting alogrithm => previous value counting system
def counting(s):
	# uniform string 
	s = list(s)
	cc = []		# contigous character counter
	c = 1
	for i in range(1,len(s)):
		if s[i] == s[i-1]:
			c += 1
		if s[i] != s[i-1]:
			cc.append((s[i-1],c))
			c = 1
		# print(s[i-1],i-1,i,s[i],cc,c)
	else:
		cc.append((s[i],c))
	return cc

# queries to say 'Yes' or 'No'
def weightedUniformStrings(s, q):
	# alphabet encoding
    ws = {y:x for x,y in enumerate(string.ascii_lowercase,start=1)}

    # contigous character counting
    cc = counting(s)
    print(cc)
    print(ct(s))

    # weightedUniformStrings
    wus = []	
    for i in cc:
    	a,b = i
    	comb = [ws[a]*i for i in range(1,b+1)]
    	wus.extend(comb)
    print(wus)


    # queries 
    for i in q:
    	if i in wus:
    		wus.remove(i)
    		yield 'Yes'
    	else:
    		yield 'No'

wus = weightedUniformStrings(si,q)
t,f = 0,[0,[]]
for x,y in enumerate(wus):
	if y == o[x]:
		t += 1
	else:
		f[0] += 1
		f[1].append((q[x],y,o[x]))
	print(x,'=>',y == o[x])

print(t,f)

print(si[:5])
print(q[:5])
print(o[:5])


#==================another alogrithm=================#
def weightedUniformStrings(s, queries):
    l = string.ascii_lowercase
    d = {}
    for i,j in enumerate(l,1):
        d[j] = i
    e = ct(s)
    w_c = []
    w = []
    for i,j in e.items():
        for k in range(1,j+1):
            w_c.append(i*k)
            w.append(d[i]*k)
    # print('words = ',w)
    # print('queries = ',queries)
    for i in queries:
        if i in w:
            print('Yes')
        else:
            print('No')
        break



# weightedUniformStrings(si,o)




















