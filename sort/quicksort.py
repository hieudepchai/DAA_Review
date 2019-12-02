def partition(arr, start, end):
    left_index = start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] < pivot:
            #swap
            arr[left_index], arr[i] = arr[i], arr[left_index]
            left_index+=1
    arr[end] = arr[left_index]
    arr[left_index] = pivot
    return left_index
            
def QuickSort(arr, start, end):
    if start < end:
        pivot_position = partition(arr,start, end)
        QuickSort(arr,start, pivot_position - 1)
        QuickSort(arr, pivot_position + 1, end)

if __name__ == "__main__":
     arr = [9,7,8,3,2,1]
     QuickSort(arr,0, len(arr) - 1)
     print(arr)