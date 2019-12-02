def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        iMin = i
        for j in range(i+1, n):
           if arr[j] < arr[iMin]:
               iMin = j
        arr[i], arr[iMin] = arr[iMin], arr[i]
if __name__ == "__main__":
    arr = [9,7,8,3,2,1]
    SelectionSort(arr)
    print(arr)

