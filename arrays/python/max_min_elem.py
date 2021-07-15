#to find the maximum and minimum alements from an array

#method 1
# sort nlog n and return arr[0] and arr[len(arr)-1]

def max_min_1(arr):
    arr.sort()
    return arr[0], arr[len(arr)-1]

#method 2
#iterative approach- compare each element as we iterate
#number of comparsions = 1+2(n-2)
# simple linear search O N

def max_min_2(arr):
    if not arr:
        return
    if len(arr)==1:
        return arr[0], arr[0]
    if arr[0]>arr[1]:
        max_elem = arr[0]
        min_elem = arr[1]
    else:
        max_elem = arr[1]
        min_elem = arr[0]
    for i in range(2,len(arr)):
        if arr[i]>max_elem:
            max_elem= arr[i]
        if arr[i]< min_elem:
            min_elem = arr[i]
    return min_elem, max_elem

#method 3 recursive
# tournament method - divide array into two parts and 
# compare max and min of each part to get max min of whole array

def max_min_3(arr, start, end):
    max_elem = arr[start]
    min_elem = arr[start]
     
    if start == end:
        max_elem = arr[start]
        min_elem = arr[start]
        return (min_elem, max_elem)
         
    elif end == start + 1:
        if arr[start] > arr[end]:
            max_elem = arr[start]
            min_elem = arr[end]
        else:
            max_elem = arr[end]
            min_elem = arr[start]
        return (min_elem, max_elem)
    else:         
        # If there are more than 2 elements
        mid = int((start + end) / 2)
        min1, max1 = max_min_3(arr,start, mid)
        min2, max2 = max_min_3(arr, mid + 1, end)
 
    return  min(min1, min2), max(max1, max2)


print(max_min_1([1,2,3,4]))
print(max_min_2([1,2,3,4]))
print(max_min_3([1,2,3,4],0,3))


