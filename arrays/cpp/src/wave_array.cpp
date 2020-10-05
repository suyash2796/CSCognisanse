//sort a given unsorted array of integers, in wave form.
// An array is in wave form when array[0] >= array[1] <= array[2] >= array[3] <= array[4] ...

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> arr={1,2,3,4,52,3,5,4};
    sort(arr.begin(),arr.end());
    for(int i=0;i<arr.size()-1;i=i+2)
    swap(arr[i],arr[i+1]);
    for(auto item:arr) cout<< item;

    return 0;
}