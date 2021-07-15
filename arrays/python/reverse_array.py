# iterative solution
#O(N)
def reverse_iterative(array):
    size = len(array)
    start=0
    end=size-1
    while start<end:
        array[start],array[end] = array[end],array[start]
        start+=1
        end-=1
    return array

# recursive solution
#O(N)
def reverse_recursive(array, start, end):
    if start>=end:
        return
    array[start],array[end] = array[end],array[start]
    reverse_recursive(array, start+1, end-1)
    

print(reverse_iterative([1,2,3,4]))
arr=[1,2,3,4]
reverse_recursive(arr,0,3)
print(arr)
        