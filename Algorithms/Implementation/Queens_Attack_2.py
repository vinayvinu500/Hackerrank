# https://www.hackerrank.com/challenges/queens-attack-2/problem
# queen chess board with row & column
# n will be the nxn chess board with (rxc)
# k will be the obstacles with (rxc)

"""
Queen Moves
Up
Down
Left
Right
Diagonal left, right
Obstacles block
"""

#=================================================#
# n = rxc, rq, cq, ki 
n = 8
r = n
c = n
rq, cq = 4,4
ki = [[2,4],[4,2],[6,4],[4,6],[6,2],[2,2],[2,6],[6,6]]

#=================================================#
# Board Structure
board = [[0]*n for _ in range(n)]

for i,j in enumerate(board):
    # print(abs(i-n),j) # row
    for k,l in enumerate(j):
        board[i][k] = [abs(i-n),k+1,0] # value
# print('  ','  '.join(list(map(str,range(1,n+1))))) # column

#=================================================#
# Representation
def chess(board):
    print()
    print('Chess Board')
    for i,j in enumerate(board):
        print(n-i,end=' ')
        for k,l in enumerate(j):
            print(l[-1],end=' ')
        print()
    print(' ',' '.join(list(map(str,range(1,n+1)))))
    print()

#=================================================#
# Queen
def queen(rq,cq,b,ki):
    print('Queen Attack ')
    print('queen pos  = ',rq,cq)
    print()
    #==============================================#
    # queen diagonal
    # left_down(ld), left_up(lu), right_up(ru), right_down(rd)
    ld = [] # (rq,cq) both -1
    lu = [] # (rq,cq) rq +1 and cq -1
    ru = [] # (rq,cq) both +1
    rd = [] # (rq,cq) rq -1 and cq +1
    
    for i in range(1,n+1):
        # right diagonal
        ld.append([rq-i,cq-i])
        ru.append([rq+i,cq+i])

        # left diagonal
        lu.append([rq+i,cq-i])
        rd.append([rq-i,cq+i])
    # diagonal
    for o1 in range(n):
        for i in b:
            for j in i:
                # left_down diagonal
                if j[0] == ld[o1][0] and j[1] == ld[o1][1] and j[2] != 'x':
                    j[-1] = 1
                # left_up diagonal
                if j[0] == lu[o1][0] and j[1] == lu[o1][1] and j[2] != 'x':
                    j[-1] = 1
                # right_up diagonal
                if j[0] == ru[o1][0] and j[1] == ru[o1][1] and j[2] != 'x':
                    j[-1] = 1
                # right_down diagonal
                if j[0] == rd[o1][0] and j[1] == rd[o1][1] and j[2] != 'x':
                    j[-1] = 1

    #==============================================#
    # queen position's
    for i,j in enumerate(b):
        for k,l in enumerate(j):
            # queen position
            if rq == l[0] and cq == l[1] and (l[2] == 0 or l[2] == 'x'):
                l[-1] = 9
            # up and Down , left and right
            if cq == l[1] and rq != l[0] and l[2] != 'x':
                l[-1] = 1
            if rq == l[0] and cq != l[1] and l[2] != 'x':
                l[-1] = 1
            
    #==============================================#
    # queen obstacles
    print('Obstacles')
    print(ki)
    print()
    if len(ki) != 0:
        # o = []
        # for i in range(1,n+1):
        #     for j in ki:
        #         # print(j,i,j[0]-i,j[1]-i)
        #         if j[0]+i < n and j[1]+i < n: 
        #             o.append([j[0]+i,j[1]+i])
        #     # print()
        # print(o)
        for i in b:
            for ob,j in enumerate(i,1):
                # obstacles
                for o1 in ki:
                    # print(o1,o1[0]-ob,o1[1]-ob)
                    if j[0] == o1[0] and j[1] == o1[1] and (j[2] == 0 or j[2] == 1):
                        j[-1] = 'x'
                #     print(ob,o1[0]-ob,o1[1]-ob)
                #     if j[0] == o1[0]-ob and j[1] == o1[1]-ob and j[2] == 1:
                #         j[-1] = 0
                # print()
        # backward obstacles
        # for o2 in o:
        #     print(o2)
                #     if  j[0] == o2[0] and j[1] == o2[1] and j[2] == 1:
                #         j[-1] = 0

#=================================================#
# Results
chess(board)
queen(rq,cq,board,ki)
chess(board)