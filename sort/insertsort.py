def InsertionSort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j=i-1
        while j>=0 and arr[j] > key:
            arr[j+1] =arr[j]
            j-=1
        arr[j+1] = key
if __name__ == "__main__":
    arr = [9,7,8,3,2,1]
    InsertionSort(arr)
    print(arr)