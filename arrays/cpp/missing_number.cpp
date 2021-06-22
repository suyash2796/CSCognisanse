#include<iostream>
#include<vector>
using namespace std;


//find missing number in integer array of n natural numbers
//when there is no dupe in array
int main(){
    vector<int> arr = {1,2,3,4,6};
    int size = arr.size();
    int n_sum = (size+1)*(size+2)/2;
    int arr_sum=0;
    for(int i:arr){
        arr_sum = arr_sum+i;
    }
    cout<<n_sum - arr_sum<<endl;
    return 0;

}