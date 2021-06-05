#An array is monotonic if it is either monotone increasing or monotone decreasing.

#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
#An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

#Return true if and only if the given array nums is monotonic.

#O(N) time and O(1) space solution

def check_monotone(array):
    if not array:
        return True
    size = len(array)
    i=1
    j=1
    curr= array[0]
    for k in range(1, size):
        if curr>=array[k]:
            i+=1
        if curr<=array[k]:
            j+=1
        curr = array[k]
    
    if i==size or j==size:
        return True
    return False

if __name__ == '__main__':
    test = [
            [1,2,2,5,6,6,8],
            [1,2,1,5,6,6,8],
            [-1,1,2,2,5,6,6,8],
            [-1,1,2,2,5,-6,6,8],
            [1,1,1,1,1,1,1],
            [-1,-1,-1,-1,-1,-1,-1],
            [1,2],
            [1],
            [-1,-2,-3,-4,-5,-5,-6]
    ]

    for t in test:
        print(check_monotone(t))