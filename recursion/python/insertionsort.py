def insertSort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        while j >=0 and val < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val 
arr = [67, 12, 1, 6, 9]
insertSort(arr)
print(arr)