//Write a C++ program to move all negative elements of an array of integers to the end of the array 
//without changing the order of positive element and negative element.

#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> arr = {-5,8,0,2,-6,-1,4,6};
    vector<int> res;
    for (int i=0;i<arr.size();i++){
        if(arr[i]>=0){
            res.push_back(arr[i]);
        }
    }
    for (int i=0;i<arr.size();i++){
        if(arr[i]<0) res.push_back(arr[i]);
        }
    for(auto i: res)
        cout<<i;
    return 0;
}