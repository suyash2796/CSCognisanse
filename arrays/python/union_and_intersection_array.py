#find the union and intersection of two sorted array

#brute force
def find_union_intersection_brute(arr1, arr2):
    inter=[]
    for i in arr1:
        if i in arr2:
            inter.append(i)
    return inter, arr1+arr2

#ths doesnt handle dups if found in any array
def find_union_intersection(arr1, arr2):
    l=0
    r=0
    inter=[]
    union= []
    while l<len(arr1) and r<len(arr2):
        if arr1[l]==arr2[r]:
            inter.append(arr1[l])            
            union.append(arr1[l])
            l+=1
            r+=1
        elif arr1[l]>arr2[r]:
            union.append(arr2[r])
            r+=1
        else:
            union.append(arr1[l])
            l+=1
    while l < len(arr1):
        union.append(arr1[l])
        l += 1
 
    while r < len(arr2):
        union.append(arr2[r])
        r += 1

    return inter, union


if __name__ == '__main__':
    print(find_union_intersection([1,2,3],[1,2,4]))


