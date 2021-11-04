# https://www.hackerrank.com/challenges/lisa-workbook/problem

# test 0
n = 2
k = 3
arr = [4,2]


# test 1
n = 5
k = 3
arr = [4,2,6,1,10]

#=======================#
c = [] # chapters
p = [] # pages 

# while loop implementation
i = 1 # starting index -> page
j = arr[0] # ending index -> page
ind = 0 # arr[ind] -> chapter
x = 1 # chapter indexing
y = 1 # kth paging
sp = 0 # special page

# while loop 
while i < j+1:
    # pages 
    p.append(i)
    
    # representation
    print(j,i,y,x)
    
    # special page
    if i == x:
        sp += 1
    
    # chapter turn (Bug)
    if i == j and y == k:
        # chapters of pages 
        ch = lambda a: x in a[0] 
        print(ch(c))
        c.append((x,p))
        
        # bug fixed
        x -= 1
        
    
    # next indexing
    i += 1
    y += 1
    
    # kth indexing
    if y == k+1:
        # pages
        c.append((x,p))
        p = []
        
        # chapters and pages
        x += 1
        y = 1

    # arr indexing 
    if i == j+1:
        # chapters of pages 
        c.append((x,p))
        p = []
        
        x += 1
        ind += 1
        y = 1
        
        # breaking loop
        if ind == n:
            break
        i = 1
        j = arr[ind] 
        print()
      

print()
# representation of chapters 
# Bug in chapters 
for i in c:
    print(i)

print()             
print('special = ',sp)