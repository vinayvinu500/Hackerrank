#page starts with right side by 1
#backside page count 
# https://www.hackerrank.com/challenges/drawing-book/problem?h_r=internal-search


n = 5
p = 4

#pages = [[i,i+1] for i in range(n+1)][::2] #experi

book = list(range(n+1))
book.append(0)
#print(book)

pages = []
elem = []
for i in range(n//2+1):
    for j in range(2):
        elem.append(book.pop(0))
        #print(book.pop(0))
    pages.append(elem)
    elem = []
print(pages)

def st(b,p):
    start = 0
    for i in b:
        if p in i:
            return start
        start +=1

def en(b,p):
    end = 0
    for i in b[::-1]:
        if p in i:
            return end
        end +=1

a = st(pages,p)
b = en(pages,p)

print(a,b)
print(min(a,b))