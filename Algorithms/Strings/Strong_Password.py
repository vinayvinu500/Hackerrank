# https://www.hackerrank.com/challenges/strong-password/problem?h_r=internal-search

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    p = {'n','l','u','s'}
    c = set()

    for i in password:
        if i.isdigit():
            c.add('n')
        if i.islower():
            c.add('l')
        if i.isupper():
            c.add('u')
        if i in special_characters:
            c.add('s')

    sp = len(p-c)

    if n < 6:
        sp += (6-n) - sp

    return sp


# passwords
a0 = '2bbbb'
a1 = '2bb#A'
a2 = 'Ab1'
a3 = '#HackerRank'

print(minimumNumber(len(a0), a0))


'''
# https://www.hackerrank.com/challenges/strong-password/problem

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

s = '2bbb'
#s = 'Ab1'
#s = 'Vinay-01'
#s = '#HackerRank'
#s = 'Vina1'


n = len(s)
print('length = ',n)
print('string = ',s)
# criteria
"""
> at least 6 length
> at least one digit
> at least one lowercase
> at least one uppercase
> at least one special char
"""

# password characters 
p = {'s','u','l','d'} # 4 character

# available
available = set()
for i in s:
    if len(available) == 4:
        break
    if i.isupper():
        available.add('u')
    if i.islower():
        available.add('l')
    if i.isdigit():
        available.add('d')
    if i in special_characters:
        available.add('s')
print('available = ', available)

# missing
missing = p - available
print('missing = ',missing)

# length
length = abs(n - 6) + len(missing) # 1 space
print('length = ', length)

"""
if k >= 6:
    sp = len(missing)
    print('strong password = ',sp)
if n < 6:
    k = n - sp
    sp += k
    print('password = ',sp)

     
print('evaluate = ',k)   
"""
'''