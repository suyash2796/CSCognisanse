#Sort an array of 0s, 1s and 2s

#Method 1: Simple counting
# Count no. of 1's 2's 0's in array and move in respective order
# we traverse array two times, brute force O(N)

def sort_012_simple(arr):
    count0=0
    count1=0
    count2=0
    for i in arr:
        if i==1:
            count1+=1
        if i==0:
            count0+=1
        if i==2:
            count2+=1
    
    for i in range(0,count0):
        arr[i]=0
    for i in range(count0, count0+count1):
        arr[i]=1
    for i in range(count0+count1, count1+count0+count2):
        arr[i]=2
    return arr

#method 2
#only one arr traversal is needed
#keep window of low mid and high range for three numbers respectively

def sort012_ranges(arr):
    low=0
    mid=0
    high = len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    return arr

if __name__=='__main__':
    print(sort_012_simple([1,2,2,0,0,1,1,2,0,0]))
    print(sort012_ranges([1,1,1,0,0,1,0,2,1,2,1,0]))