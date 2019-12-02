def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
if __name__ == "__main__":
    arr = [9,7,8,3,2,1]
    BubbleSort(arr)
    print(arr)