#validating_uid
# https://www.hackerrank.com/challenges/validating-uid/problem?h_r=internal-search

import re
# constraints
# upper() >= 2
# isnum() >= 3
# [a-z,A-Z,0-9]
# no character should repeat
# len == 10

def valid_check(s):
    if re.search(r'[a-zA-Z0-9]{10}',s) and [s.count(i) for i in s].count(2) == 0:
        if re.search(r'[A-Z]{2}',s) and re.search(r'[0-9]{3}',s):
            m = re.search(r'[^a-zA-Z0-9]',s)
            return 'Valid' if m is None else 'Invalid'
    return "Invalid"
    
#===========================#
    """
    u = re.search(r'[A-Z]{2}',s) if l else 0
    d = re.search(r'[0-9]{3}',s) if u else 0
    m = re.search(r'[^a-zA-Z0-9]',s) if d else 0
    st =[s.count(i) for i in s].count(2) if m is None else 1
    print("len = ",l)
    print("Cap = ",u)
    print("dig = ",d)
    print("spl = ",m)
    print("rep = ",st)
    print()
    return 'Valid' if st == 0 else 'Invalid'
    """
    
"""
def valid(s):
    if len(s) == 10:
        u = [i.isupper() for i in s]
        if u.count(True) >=2:
            n = [i.isdigit() for i in s]
            if n.count(True) >= 3:
                m = re.search(r'[^a-zA-Z0-9]+',s)
                if not m:
                    st = [s.count(i) for i in s]
                    if 2 in st:
                        return 'Invalid'
                    else:
                        return 'Valid'
                
    return 'Invalid'

"""
uid = [input() for _ in range(int(input()))]
uid = list(map(valid_check,uid))
for i in uid:
    print(i)
    
    
"""
2
B1CD102354
B1CDEF2354
"""
