# Given an array arr[] and a number K where K is smaller than size of array, 
# the task is to find the Kth smallest element in the given array. 
# It is given that all array elements are distinct.


#solution1
#nlogn sorting solution
def kth_smalllest(arr,k):
    arr.sort()
    return arr[k-1]

# Other possible solutions Techniques:
# Brute Force approach : Using sorting
# Using Min-Heap
# Using Max-Heap
# Quick select : Approach similar to quick sort
