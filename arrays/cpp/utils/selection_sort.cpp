#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> selection_sort(vector<int> arr, int size){
    for (int i =0;i<arr.size();i++){
        int min_index = i;
        for(int j= i+1;j<arr.size();j++){
            if(arr[j] < arr[min_index])  
                min_index = j;
        }    
        if(i != min_index)  
            swap(arr[i], arr[min_index]);        
    }
    return arr;
}