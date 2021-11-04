
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=internal-search

import string


def print_rangoli(n):
    # formulae
    a = string.ascii_lowercase   #alpha
    f = (n+n-1)*2 - 1            #width
    #shape
    if n == 1:
        print(a[n-f].center(f,'-'))
    else:
        for i in range(n):
            x = a[n-i-1]
            i = a.index(x)
            y = '-'.join(a[n-1:i:-1])
            z = '-'.join(a[i+1:n])
            print((y+'-'+x+'-'+z).center(f,'-'))
    for i in range(1,n):
        x = a[i]
        i = a.index(x)
        y = '-'.join(a[n-1:i:-1])
        z = '-'.join(a[i+1:n])
        print((y+'-'+x+'-'+z).center(f,'-'))

n = input()
print_rangoli(i)


#===========================#    
#backup
def backup_up(r,s):
    '''
    f : (size:r,start:s)
    func(n,i)
    '''
    x = a[r-s-1]
    i = a.index(x)
    y = '-'.join(a[r-1:i:-1])
    z = '-'.join(a[i+1:r])
    print((y+'-'+x+'-'+z).center(f,'-'))
