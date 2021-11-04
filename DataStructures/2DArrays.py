import numpy as np
# https://www.hackerrank.com/challenges/2d-array/problem?h_r=internal-search

arr = []

for _ in range(6):
    arr.append(list(map(int, input().strip().split())))
    pass

arr = np.array(arr)

print(arr)
"""
hour glass are 16 in 6x6 matrix 
[
    1 1 1
      1
    1 1 1
]

"""
# print(arr.size) # no of elements in matrix

# one hourglass
# hourglass = arr[3, 2] + arr[3, 3] + arr[3, 4] + arr[4, 3] + arr[5, 2] + arr[5, 3] + arr[5, 4]
#
# print(hourglass)

# sample hourglass
# sample = arr[0, 0] + arr[0, 1] + arr[0, 2] + arr[1, 1] + arr[2, 0] + arr[2, 1] + arr[2, 2]
# samples = arr[i,j] + arr[i,j] + arr[i, j] + arr[i+1,1] + arr[i+2,j] + arr[i+2,j] + arr[i+2,j]

"""
method 1
# for loop integration
total = []
mi = 0
up = []
do = []
for i in range(4):
    # first [0,1,2] to [3,1,2]
    for j in range(3):
        u = arr[i,j]
        m = arr[i+1,mi+1]
        d = arr[i+2,j]
        up.append(u)
        do.append(d)
        pass
    for m in range(1,6):
        mid = arr[i+1,m]
    print('====')

    print(up)
    up = []
    print('    ',mid)
    print(do)
    do = []

    print('====')
"""

# for loop integration
"""
sample 
top - bottom = range(0,4)
times => range(0,3)
upper => range(0,6)
middle => range(1,5)
lower => range(0,6)
"""
# for i,j in enumerate(arr):
#     print(i,j)
#     for k,l in enumerate(j):
#         print(k,l)
hourGlass = []
up = []
mi = []
do = []
lin = 0
ind = 0
"""
for i, j in enumerate(arr):
    print(i, j)
    for k, l in enumerate(j):
        print(k, l)

        u = arr[i, k]
        up.append(u)
        pass
    print(up)
    up.clear()
    pass
"""


for o in range(4):
    '''
    # middle
    for k in range(1, 5):
        m = arr[lin + 1, k]
        mi.append(m)
        pass
    # print(mi)
    # mi.clear()
    '''
    for i in range(4):
        # up and down
        for j in range(3):
            # print(lin, j + ind)
            u = arr[lin, j + ind]
            d = arr[lin + 2, j + ind]
            up.append(u)
            do.append(d)
        pass
        print('===')
        print(up)
        iterationUp = sum(up)
        up.clear()

        print(arr[lin+1,i+1])
        iterationMid = arr[lin+1, i+1]

        print(do)
        iterationDow = sum(do)
        do.clear()
        print('===')
        ind += 1

        # summation of Hourglass
        hg = iterationUp + iterationMid + iterationDow
        hourGlass.append(hg)
    pass
    lin += 1
    ind = 0
# for loop end

hourGlass = max(hourGlass)
print(hourGlass)
"""
Examples
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

 1  2  3  4  5  6
 7  8  9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36
"""

