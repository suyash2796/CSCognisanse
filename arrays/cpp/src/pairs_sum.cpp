//Write a C++ program to find the number of pairs of integers
// in a given array of integers whose sum is equal to a specified number.
#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> arr = {1,2,3,4,6,8,1,5,6};
    int sum  = 5;
    for(int i=0;i<arr.size();i++){
        for(int j=0;j<arr.size();j++){
            if(arr[i]+arr[j]==sum)
            cout<<'('<<i<<','<<j<<')'<<"\n";
        }
    }
    return 0;
}