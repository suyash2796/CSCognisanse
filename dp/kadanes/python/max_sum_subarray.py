def max_sum_subarray(array):
    max_ending_here = array[0]
    max_so_far = array[0]
    for num in array[1:]:
        max_ending_here = max(max_ending_here+num, num)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


if __name__=='__main__':
    array = [1,2,-1,3,5,-9,-2]
    max_num = max_sum_subarray(array)
    print(max_num)