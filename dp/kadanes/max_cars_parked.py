def max_cars_parked(array):
    arr_len = len(array)
    parking_register = [[0,True] for i in range(2 * arr_len)]
 
    for i in range(arr_len):
        parking_register[2 * i] = [array[i][0], True]
        parking_register[2 * i + 1] = [array[i][1], False]
    
    parking_register.sort()

    curr_cnt = 0
    final_cnt = 0

    for i in range(len(parking_register)):
        if parking_register[i][1]==True:
            curr_cnt+=1
        else:
            if curr_cnt> final_cnt:
                final_cnt = curr_cnt
            curr_cnt-=1
    return final_cnt


if __name__=='__main__':
    array = [ [ 912, 1119 ],
         [ 1217, 1219 ],
         [ 1023, 1024 ],
         [1023,1027]]
    print(max_cars_parked(array))
