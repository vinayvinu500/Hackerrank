# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?h_r=profile

#input
n = int(input())
e =[input() for _ in range(n)]
#name
name = [i.split()[0] for i in e]
#user
user = [i.split()[1].split('@')[0].replace('<','') for i in e]
#email
email = [i.split()[1].split('@')[1].split('.')[0] for i in e]
#extension
exts = [i.split()[1].split('@')[1].split('.')[1].replace('>','') for i in e]
#email list
r = list(zip(name,user,email,exts))
##name validation
nm = (lambda x,y: x.upper() == y.upper() )
##user validation
usr =(lambda x: ''.join([i for i in x if i in map(chr,range(65,91)) or i in map(chr,range(97,123)) or i in map(str,range(0,10)) or i in chr(95) or i in chr(45)]) == x)
##website validation
web = (lambda x: "".join([i for i in x if i in map(chr,range(65,91)) or i in map(chr,range(97,123)) or i in map(str,range(0,10))]) == x)
##extension validation
ext = lambda x: ''.join([i for i in x if (len(x) == 3) and i in map(chr,range(65,91)) or i in map(chr,range(97,123))]) == x
#validation
for i in r: 
    if all([
nm(i[0],i[1]),
usr(i[1]),
web(i[2]),
ext(i[3])
]):
        print(f"{i[0]} <{i[1]}@{i[2]}.{i[3]}>")



'''
#email validation
validate = sorted([i[0]+'@'+i[1]+'.'+i[2] 
for i in email if all([
usr(i[0]),web(i[1]),ext(i[2])])])
print(validate)

'''
"""
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
"""