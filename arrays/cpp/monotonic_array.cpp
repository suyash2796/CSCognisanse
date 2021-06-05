//An array is monotonic if it is either monotone increasing or monotone decreasing.

//An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
//An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

//Return true if and only if the given array nums is monotonic.

//O(N) time and O(1) space solution

#include<iostream>
#include<vector>
using namespace std;

int main(){
    //todo
    vector<int> arr = {1,2,3,-4,7,9,10};
    int size = arr.size();
    int i =1;
    int j=1;
    int first = arr[0];
    for(int k=1;k<size;k++){
        if(arr[k]>=first)
            i++;
        if(arr[k]<=first)
            j++;
        first = arr[k];
    }
    if(i==size || j==size)
        cout<<"monotonic array"<<endl;
    else
        cout<<"Non-monotonic array"<<endl;    
    
    return 0;
}