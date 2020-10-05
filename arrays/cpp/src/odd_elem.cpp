//Write a C++ program to find the numbers which occurs odd number of times of a given array of positive integers.
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

//TODO:
// remove dups

int main(){
    vector<int> arr = {1,2,2,3,5,3,3,7,5,5,5,5};
    for(auto item:arr){
        if (count(arr.begin(), arr.end(),item)%2!=0){
            cout<<item<<' ';
        }
    }
    return 0;
}