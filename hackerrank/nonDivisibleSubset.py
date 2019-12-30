s = [1, 7, 2, 4, 9, 16, 8, 3,11,12,13]

def nonDivisibleSubset(k, s):
    n = len(s)
    remainder = [ num % k for num in s]
    count_remainder = {0:0}
    res = 0
    for i in range (1, int(k/2)+1):
        count_remainder[i] = count_remainder[k-i] = 0
    print(count_remainder)
    for r in remainder:
        count_remainder[r] +=1
    print(count_remainder)
    for i in range (1, int(k/2)+1):
        if count_remainder[i] < count_remainder[k-i]:
            res+= count_remainder[k-i]
        else:
            res+= count_remainder[i]
    if int(k/2)*2 == k:
        res = res - count_remainder[int(k/2)]+1
    if count_remainder[0] > 0:
        res+= 1
    return res
res = nonDivisibleSubset(3,s)
print(res)