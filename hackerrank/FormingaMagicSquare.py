# https://www.hackerrank.com/challenges/magic-square-forming/problem
from itertools import permutations
all_matrix = list(permutations([i for i in range(1,10)]))
magic_square = []
s = [[5,3,4], [1,5,8], [6,4,2]]
flat_s =  [i for sub in s for i in sub]
#find all magic squares
def isMagicSquare(matrix):
    for i in range(0,7,3):
        if sum(matrix[i:i+3]) !=15:
            return 0
    for i in range(3):
        if sum(matrix[i:i+7:3]) !=15:
            return 0
    if sum(matrix[0:9:4]) !=15 or sum(matrix[2:7:2]) !=15:
        return 0
    return 1

for matrix in all_matrix:
    if isMagicSquare(matrix) ==1:
        magic_square.append(matrix)
min = 100000
for mq in magic_square:
    total = sum([abs(x1 -x2) for (x1,x2) in zip(mq, flat_s)])
    if total < min:
        min = total
print(min)