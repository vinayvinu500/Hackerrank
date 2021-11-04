from collections import Counter
# https://www.hackerrank.com/challenges/most-commons/problem?h_r=internal-search

s = 'aabbbccde'
# s = 'qwertyuiopasdfghjklzxcvbnm'
print(s)

def key(s):
	print(s)

def logo(s):
	print(Counter(s))

	# log = sorted([str(j)+i for i,j in Counter(s).items()],key=lambda x: x.isdigit,str.isalpha) # i = alphabet, j = number
	log_ = sorted([i+str(j) for i,j in Counter(s).items()],key=lambda x: x.isdigit()==x.islower())
	# print(log)
	print(log_)

logo(s)
# key(s)

# from collections import Counter

# # https://www.hackerrank.com/challenges/most-commons/problem
# s = 'google'
# # s = 'aabbbccde'
# # s = 'qwertyuiopasdfghjklzxcvbnm'

# # max value first
# # second max value if equal lexicographic order

# c = Counter(s)
# print(c)
# print(c.items())
# d = sorted(c.items(), key=lambda x: x[0])
# print(d)

'''
from collections import Counter as ct
s = list('aabbbccde') #list(input())

s = ct(s) #counter 

key = [i for i in s.keys()]         #keys
val = [i for i in s.values()]       #values
data = [[i,j] for i,j in s.items()] #items of key:value

c = [[i,j] for i,j in data if j>=2] #most occurred

v = [i for i,j in c]  #values

for i,j in c:
    print(i,j)
    #most common characters
    if max(v):
        print(i,j)
'''