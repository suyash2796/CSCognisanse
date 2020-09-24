#include<iostream>
#include<vector>
using namespace std;
using std::vector;

vector<int> insertion_sort(vector<int> arr, int size){
    int i=0;
    int j=0;
    int key;
    for(int i=1;i<size;i++){
        key = arr[i];
        j = i-1;
        while(key<arr[j] && j>=0){
            arr[j+1] = arr[j];
            j=j-1;
        }
        arr[j+1] = key;

    }
    return arr;
}