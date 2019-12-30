#https://www.hackerrank.com/challenges/queens-attack-2/problem

def queensAttack(n, k, r_q, c_q, obstacles):
    chessboard = [[1]*n for i in range(n)]
    print('chessboard = ', chessboard)
    
    return 0
if __name__ == "__main__":
    infile = open('hackerrank/queensAttack.txt','r')
    nk = list(map(int, infile.readline().split()))
    n = nk[0]
    k = nk[1]
    rcq = list(map(int, infile.readline().split()))
    r_q = rcq[0]
    c_q = rcq[1]
    obstacles = []
    for i in range(k):
        obstacles.append(list(map(int, infile.readline().split())))
    print('n = ',n)
    print('k = ', k)
    print('r_q = ', r_q)
    print('c_q = ', c_q)
    print('obstacles = ', obstacles)
    res = queensAttack(n,k, r_q, c_q, obstacles)
    print('res = ', res)