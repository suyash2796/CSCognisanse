#Rotate array k times

#Method1
# O(N*K) - may take much time when k and n is large
def rotate_m1(arr, k):
    s = len(arr)
    if s < 1 or s == k:
        return A
    k = k % s
    for x in range(k):
        tmp = arr[s - 1]
        for i in range(s - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = tmp
    return arr


def reverse(arr, i, j):
    for idx in range((j - i + 1) // 2):
        arr[i+idx], arr[j-idx] = arr[j-idx], arr[i+idx]

#Method2
#O(N)
# the base case with K < N, the idea in this case is to split the array in two parts A and B,
# A is the first N-K elements array and B the last K elements. 
# the algorithm reverse A and B separately and finally reverse the full
# array (with the two part reversed separately). 
# To manage the case with K > N, think that every time you reverse the array N times you 
# obtain the original array again so we can just use the module operator to find where
# to split the array (reversing only the really useful times avoiding useless shifting)

def rotate_m2(arr, k):
    s = len(arr)
    if s == 0:
        return []

    k = k%s

    reverse(arr, s - k, s -1)
    reverse(arr, 0, s - k -1)
    reverse(arr, 0, s - 1)

    return arr

if __name__== "__main__":
    arr1=[1,2,3,4,5,6,7,8,9]
    arr2=[1,2,3,4,5,6,7,8,9]
    print(rotate_m1(arr1,2))
    print(rotate_m2(arr2,2))