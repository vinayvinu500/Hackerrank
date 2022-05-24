# https://www.hackerrank.com/challenges/two-arrays/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
from collections import Counter as ct

A = [0,1]
B = [0,2]
k = 1

A = [2, 1, 3]
B = [7, 8, 9]
k = 10

A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
k = 5

A = [7, 6, 8, 4, 2]
B = [5, 2, 6, 3, 1]
k = 10


with open('TestCase04.txt','r') as f:
	t = int(f.readline())
	arr = []
	for i in range(t):
		n,k = list(map(int,f.readline().split()))
		a = list(map(int,f.readline().split()))
		b = list(map(int,f.readline().split()))
		arr.append((n,k,a,b))
	o = f.read().split('\n')


# Experiment
def twoArrays(k, n, a, b):
	A = sorted(a)
	B = sorted(b,reverse=True)
	if all([A[i] + B[i] >= k for i in range(n)]):
		return 'YES'
	return "NO"

    	
# n,k,a,b = arr[0]
# twoArrays(k,n,a,b),o[0]
for i in range(t):
	n,k,a,b = arr[i]
	print(i,twoArrays(k,n,a,b)==o[i])



"""
	# approach
	# x + y = k
	# x = k - y
	# y = k - y

	# method 1
    # for i in a:
    # 	x = i
    # 	y = abs(x - k)
    # 	print(x,y,x+y,a,b)
    # 	if y in b: # x+y >= k
    # 		print(y)
    # 		b.remove(y)
    # print(len(b) == 0)

    # method 2 => bug found
    # a.sort()
    # b.sort() 

    # print(n,k)
    # d = {i:list(filter(lambda x: x+i >= k,b)) for i in a}
    # print(d.keys(),len(d.keys()))
    # print(len(d))
    # print(all(d.values()))
    # print()

    # method 3 => minor bug => 0 [7, 6, 8, 4, 2] [2, 6, 3, 1, 5] => a[i]=> 7 is satisfied by [1,2,4]
    # for i in range(n):
    # 	b.append(b.pop(0))
    # 	# print(i,a[:5],b[:5],[a[i]+b[i] >= k for i in range(n)][:5])
    # 	if all([a[i]+b[i] >= k for i in range(n)]):
    # 		print(a,b)
    # 		return 'YES'
    # return 'NO'

"""
