
def merge(arr, start, mid, end):
    leftArr = [ arr[i] for i in range(start, mid+1)]
    rightArr =[arr[i] for i in range(mid+1, end+1)]
    nLeft = len(leftArr)
    nRight = len(rightArr)
    iLeft = 0
    iRight = 0
    iArr = start
    while iLeft < nLeft and iRight< nRight:
        if leftArr[iLeft] < rightArr[iRight]:
            arr[iArr] = leftArr[iLeft]
            iLeft+= 1
        else:
            arr[iArr] = rightArr[iRight]
            iRight+=1
        iArr+=1
    while iLeft < nLeft:
        arr[iArr] = leftArr[iLeft]
        iArr+=1
        iLeft+=1    
    while iRight < nRight:
        arr[iArr] = rightArr[iRight]
        iArr+=1
        iRight+=1
    

def merge_sort(arr,start, end):
    if (start < end):
        mid = int((end+start)/2)
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def test(arr):
    arr[0]=111

if __name__ == "__main__":
    A = [7,9,1,1,11,2,8]
    B = [9,7, 8, 3, 2, 1]
    for val in B:
        print(val, end=" ")
    print()
    merge_sort(B,0,len(B)-1)
    for val in B:
        print(val, end=" ")