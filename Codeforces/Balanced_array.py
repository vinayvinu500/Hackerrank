"""Balanced Array"""
#info
#https://www.hackerrank.com/contests/world-codesprint-11/challenges/balanced-array

#n is a even number
n = 4
#add num to left to balanced array
arr = [1,2,5,2,4,2]
arr = [1,2,1,2,1,3]
arr =[10,20]
arr = [1,2,2,3]
#algorithm
e = len(arr) // 2
l = arr[:e]
r = arr[e:]
if l == r:
    print(0)
d = abs(sum(l) - sum(r))
print(d)

#==========================#
n = 4
arr=[1,2,3,3]
print('arr = ',arr)
print()

#left
left = [0]
x=0
for i in range(1, len(arr)):
    x+=arr[i-1]
    left.append(x)
    print('x = ',x)
    print('left = ',left)
print(left)
print()

#right
right = [0]
y=0
arr=[1,2,3,3]
arr.reverse()
for i in range(1, len(arr)):
    y+=arr[i-1]
    right.append(y)
    print('y = ',y)
    print('right = ',right)
right.reverse()
print(right)
print()

# balanced array
arr.reverse()
for i in range(1, len(arr)):
    print(left[i],right[i])
    if left[i]==right[i]:
        print()
        print ('pivot = ',i)
        print()
        pass

