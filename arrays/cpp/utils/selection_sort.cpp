#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
using std::cout;

int main(){
    vector<int> arr = {1,3,2,7,8,1,4,6,2,36,6,5};
    cout<<"input array: \n";
    for(auto item:arr){
        cout<<item<<",";
    }
    for (int i =0;i<arr.size();i++){
        int min_index = i;
        for(int j= i+1;j<arr.size();j++){
            if(arr[j] < arr[min_index])  
                min_index = j;
        }    
        if(i != min_index)  
            swap(arr[i], arr[min_index]);        
    }
    cout<<"\n \nsorted array"<<"\n";
    for(auto item:arr){
        cout<<item<<",";
    }
    cout<<"\n";
    return 0;
}