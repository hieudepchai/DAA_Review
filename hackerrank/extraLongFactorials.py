def extraLongFactorials(n):
    if n < 2:
        return 1
    fact = 1
    for i in range(1,n+1):
        fact*= i
    return fact
print(extraLongFactorials(100))