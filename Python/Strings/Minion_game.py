# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=false
import string

s = 'BANANA'
s = 'BAANANAS'
n = len(s)

# Kevin has to make words starting with vowels. 
# Stuart has to make words starting with consonants. and Y is also a Consonant
# A player gets +1 point for each occurrence of the substring in the string .

v = ('A','E','I','O','U')
c = tuple(filter(lambda x: x not in v ,string.ascii_uppercase))

print('Vowels => ',v)
print('Consonants => ',c)
print('String => ',list(s))


# KEVIN
kv = []
a = []

# STUART
st = []
b = [] 

# finding letters in String & Starting Letters => vowels and consonants
for i,j in enumerate(s):
	if j in v:
		a.append((i,j))
	elif j in c:
		b.append((i,j))

print('Kevin  => ',a)
print('Stuart => ',b)


# Optimized Code
# finding letters and starting with them for both players
# for i,j in enumerate(s):
#     # kevin
#     if j in v:
#         kv += n-i
        
#     # stuart
#     elif j in c:
#         st += n-i

# kevin 
print('Kevin Play...')
o = ''
for i in range(len(a)):
	x,y = a[i] # (1,'A')
	kv.append(y)
	o+= y
	for j in range(x+1,n):
		o += s[j]
		print(j,o)
		kv.append(o)
	o = ''


# stuart
print('\nStuart Play...')
for i in range(len(b)):
	x,y = b[i]
	st.append(y)
	o+= y
	for j in range(x+1,n):
		o+=s[j]
		print(j,o)
		st.append(o)
	o = ''

print('\nWinner => ',end='')
# result
if len(kv) > len(st):
    print(f'Kevin {len(kv)}')
elif len(st) > len(kv):
    print(f'Stuart {len(st)}')
else:
    print('Draw')


print('Kevin  => ',kv,'\nScore  => ',len(kv))
print('Stuart => ',st,'\nScore  => ',len(st))
