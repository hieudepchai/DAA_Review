# https://www.hackerrank.com/challenges/a-very-big-sum/problem

def aVeryBigSum(ar):
    return sum(ar)
if __name__ == "__main__":
    infile = open('hackerrank/averybigsum.txt','r')
    n = int(infile.readline())
    arr = list(map(int, infile.readline().split()))
    res = aVeryBigSum(arr)
    print(res)
 