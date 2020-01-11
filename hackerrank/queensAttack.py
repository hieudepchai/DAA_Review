#https://www.hackerrank.com/challenges/queens-attack-2/problem
import numpy as np
def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0 
    r_q = n-1 - (r_q-1)
    c_q -= 1
    for i in range(k):
        obstacles[i][0] = n-1 - (obstacles[i][0]-1)
        obstacles[i][1] -= 1
    print('In funcions: ')
    print('n = ',n)
    print('k = ', k)
    print('r_q = ', r_q)
    print('c_q = ', c_q)
    print('obstacles = ', obstacles)
    #
    for r in range(r_q -1 , -1, -1):
        # if chessboard[r][c_q] == 1:
        #     break
        if [r,c_q] in obstacles:
            break
        count+=1
    for r in range(r_q+1, n):
        # if chessboard[r][c_q]==1:
        #     break
        if [r, c_q] in obstacles:
            break
        count+=1
    #
    for c in range(c_q-1, -1, -1):
        # if chessboard[r_q][c]==1:
        #     break
        if [r_q, c] in obstacles:
            break
        count+=1
    for c in range(c_q+1,n):
        # if chessboard[r_q][c]==1:
        #     break
        if [r_q, c] in obstacles:
            break
        count+=1
    #
    r, c = r_q, c_q 
    while True:
        r-=1
        c-=1
        if (r<0) or (c<0) or [r,c] in obstacles:
            break
        count+=1
    r, c = r_q, c_q
    while True:
        r+=1
        c+=1
        if (r==n) or (c==n) or [r,c] in obstacles:
            break
        count+=1
    #
    r, c = r_q, c_q
    while True:
        r-=1
        c+=1
        if (r<0) or (c==n) or [r,c] in obstacles:
            break
        count+=1
    r, c = r_q, c_q
    while True:
        r+=1
        c-=1
        if (r==n) or (c<0) or [r,c] in obstacles:
            break
        count+=1
    return count
if __name__ == "__main__":
    infile = open('queensAttack.txt','r')
    nk = list(map(int, infile.readline().split()))
    n = nk[0]
    k = nk[1]
    rcq = list(map(int, infile.readline().split()))
    r_q = rcq[0]
    c_q = rcq[1]
    obstacles = []
    for i in range(k):
        obstacles.append(list(map(int, infile.readline().split())))
    print('Input: ')
    print('n = ',n)
    print('k = ', k)
    print('r_q = ', r_q)
    print('c_q = ', c_q)
    print('obstacles = ', obstacles)
    res = queensAttack(n,k, r_q, c_q, obstacles)
    print('res = ', res)