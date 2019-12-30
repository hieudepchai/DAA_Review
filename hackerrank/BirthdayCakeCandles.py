#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
ar =[8] 
def birthdayCakeCandles(ar):
    max = ar[0]
    count = {}
    count[max]=1
    l = len(ar)
    for i in range(1,l):
        if ar[i] > max:
            max = ar[i]
            count[max] = 1
        elif ar[i] ==max:
            count[max] += 1
    return count[max]
print(birthdayCakeCandles(ar))