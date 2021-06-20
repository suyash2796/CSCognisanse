#find the pair of integer in an array whose sum is equal to given number

#solution using hash table
#O(N) space O(N) time
def find_pair(arr, n):
    sol={}
    for i in arr:
        y=n-i
        if y in sol:
            return [y,i]
        sol[i]=True
    return []

#sliding window approach
def find_pair_2(arr,n):
    arr.sort()#log(n)
    left=0
    right=len(arr)-1
    while True:
        s= arr[right]+arr[left]
        if s>n:
            right-=1
        elif s<n:
            left+=1 
        else:
            return [arr[left], arr[right]]
    return[]

if __name__ == '__main__':
    arr = [1,2,3,5]
    print(find_pair(arr, 8))
    print(find_pair_2(arr, 8))

