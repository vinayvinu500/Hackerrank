# left rotation
# https://www.hackerrank.com/challenges/three-month-preparation-kit-array-left-rotation/problem?h_r=internal-search

d = 10
arr = [1,2,3,4,5,6,7,8,9,10]
#print(arr[d:]+arr[:d])
print(arr)
for i in range(d):
    arr.append(arr.pop(0))
arr = list(map(str,arr))
print(' '.join(map(str,arr)))

arr = [arr.pop(0) for _ in range(2)]
print(arr)