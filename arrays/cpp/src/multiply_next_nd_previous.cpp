//multiply all elements with adjacent elements except first and last elements

#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> arr = {1,2,3,4,5,6,7};
    for(int i=1;i<arr.size()-1;i++){
        arr[i] = arr[i-1]*arr[i+1]*arr[i];
    }
    for(auto item:arr)
    cout<<item<<'\n';
    return 0;
}