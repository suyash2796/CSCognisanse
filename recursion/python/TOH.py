def TowerOfHanoi(n , from_r, to_r, aux_r): 
    if n == 1: 
        print(from_r,"to",to_r) 
        return
    TowerOfHanoi(n-1, from_r, aux_r, to_r) 
    print("Disk",n,"from",from_r,"to",to_r)
    TowerOfHanoi(n-1, aux_r, to_r, from_r) 
       
n = 4
TowerOfHanoi(n, 'A', 'C', 'B') 