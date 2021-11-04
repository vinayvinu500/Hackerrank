# user input
# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=internal-search
length = int(input())
arr = []
for i in range(length):
    line = input().split()
    arr.append(line)

print(arr)
# matrix => 2x2
if length == 2:
    # left
    left = int(arr[0][0]) + int(arr[1][1])
    # right
    right = int(arr[0][1]) + int(arr[1][0])
    # diff
    diff = abs(abs(left) - abs(left))
    print(diff)
    pass
# matrix => 3x3
elif length == 3:
    # left
    left = int(arr[0][0]) + int(arr[1][1]) + int(arr[2][2])
    # right
    right = int(arr[0][2]) + int(arr[1][1]) + int(arr[2][0])
    # diff
    diff = abs(abs(left) - abs(right))
    print(diff)
    pass
# matrix => 4x4
elif length == 4:
    # left
    left = int(arr[0][0]) + int(arr[1][7]) + int(arr[2][14])
    # right
    right = int(arr[0][4]) + int(arr[1][7]) + int(arr[2][10])
    # diff
    diff = abs(abs(left) - abs(right))
    print(diff)
    pass


"""
array = []
Matrix
array[2][2] = [
    0 1
    0 1
]
array[3][3] = [
    0 1 2
    0 1 2
    0 1 2
]
array[4][4] = [
    0  1  2  3  4
    0  1  2  3  4
    0  1  2  3  4
    0  1  2  3  4
]
"""

"""
Example
1 2 3
4 5 6
9 8 9  
output =>
11 2 4
4 5 6
10 8 -12
output =>
"""
