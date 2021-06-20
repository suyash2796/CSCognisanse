#1st method when there is no duplicates in array
#O(N)
def find_missing_1(arr):
    size = len(arr)
    n_sum = (size+1)*(size+2)/2
    arr_sum =0
    for i in arr:
        arr_sum = arr_sum +i
    missing_num = n_sum-arr_sum
    return missing_num

#2nd method when arr contain duplicate elements
#O(nlog(n))
def find_missing_2(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i]+1>=arr[i+1]:
            continue
        return arr[i]+1


if __name__ == '__main__':
    arr_1=[1,2,3,4,6]
    print(find_missing_1(arr_1))
    arr_2= [1,2,3,3,4,4,6,6]
    print(find_missing_2(arr_2))