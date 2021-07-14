
#binary search method implementaion
#O(log n)
def binary_search(low, high, key, arr):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<key:
            low=mid+1
        elif arr[mid]>key:
            high=mid-1
        else:
            return mid+1
    return -1

if __name__== "__main__":
    n = int(input("enter number of elements of array: ")) #no of elements in array
    arr = list(map(int,input("enter {} elements seperated by space: ".format(n)).split(' '))) #enter n elements seperated by space
    arr.sort() # sort array O nlogn
    q = int(input("enter number of queries you want to do to get rank of elem in array: ")) #take number of queries as input
    queries=[]
    for i in range(q):
        qt = int(input("enter query ")) #take query elements in array
        print("rank of {} is {}".format(qt,binary_search(0,len(arr),qt, arr)))
        