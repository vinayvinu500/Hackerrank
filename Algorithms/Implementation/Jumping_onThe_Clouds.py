# Jumping on the clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


arr = [0,1,0,0,0,1,0]
arr = [0,0,1,0,0,1,0]
arr = [0,0,0,0,1,0]


s = 0
print(arr)
print(list(range(0,len(arr),2)))
print(list(range(1,len(arr),2)))


i = 0
while i < len(arr):
    print(i)
    if arr[i] == 0:    
        s += 1
    if i+2 > len(arr):
        break
    if i+2 < len(arr) and arr[i+2] != 1:
        i+= 2
    else:
        i += 1
print()        
print(s-1)    
"""
ind = arr.index(1)
print()
if ind != 2:
    for i in range(0,len(arr),2):
        if arr[i] == 1:    
            continue
        print(i)
        s += 1
else:
    for i in range(len(arr)):
        if arr[i] == 1:
            continue
        print(i)
        s += 1
print()
print(s-1)

# Jumping on clouds
# thunderheads or cumulus clouds
# 1 unit for jumping on one cloud
# if jumping on thunder cloud additional 2 unit
# game ends when character jumps on starting index
# 0 - cumulus, 1 - thunderhead

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_r=internal-search

e = 100 # energy level


c = [0,0,1,0] 
k = 2 # jump 
n = len(c)

c = [0, 0, 1, 0, 0, 1, 1, 0]
n = 8
k = 2

i = 0
while True:
    print(e,c[i%n],i)
    if c[i%n] == 1:
        e -= 3
    else:
        e -= 1
    i += k
    if i%n == 0:
        break
print(e)
"""