
# Given a value N, if we want to make change for N cents, 
# and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
# how many ways can we make the change? The order of coins doesn’t matter.
# For example, for N = 4 and S = {1,2,3},
#  there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
#  So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
#  there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
#  So the output should be 5.

def coin_change(TargetSum, denomination_array):
    #define a new array called no_of_ways and assign 0
    no_of_ways= [0 for i in range(n+1)]
    #number of ways of making 0 denomation? have to be 1, do not use any coin
    no_of_ways[0]=1
    #looping through the available coins to see what denom it could contribute in
    for i in denomination_array:
        for k in range(1,n+1):
            if i<=k:
                no_of_ways[k]+=no_of_ways[k-i] #using dynamic programming to add previously calculated solutions
    return no_of_ways[n]

if __name__=="__main__":
    denom = [1,2,3]
    n=4
    print(coin_change(4, denom))


