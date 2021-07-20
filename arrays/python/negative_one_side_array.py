#program to move all negative numbers on one side of the array
#two pointer approach
# O(N) time and O(1) space

def move_elem(array):
    left=0
    right=len(array)-1
    while left<=right:
        if array[left]<0 and array[right]<0:
            left+=1
        elif array[left]>0 and array[right]<0:
            array[left],array[right]=array[right],array[left]
            left+=1
            right-=1
        elif array[left]>0 and array[right]>0:
            right-=1
        else:
            right-=1
            left+=1
    return array

if __name__=="__main__":
    print(move_elem([-1,2,3,4,-3,-4,2,-2]))