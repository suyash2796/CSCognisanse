//Note: The format zig-zag array in form a < b > c < d > e < f.
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    vector<int> nums={1,2,3,4,5};
    int n=nums.size();
    bool ans = true;
 
    for (int i=0; i<=n-2; i++){
        if (ans){
            if (nums[i] > nums[i+1])
                swap(nums[i], nums[i+1]);
        }
        else{
            if (nums[i] < nums[i+1])
                swap(nums[i], nums[i+1]);
        }
        ans = !ans; 
    }
    for(auto item:nums) cout<<item<<",";
    return 0;
}