#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

int main(){
    vector<int> arr={1,2,3,4,5};
    int totalsum =8;
    unordered_set<int> sol;
    int i=0;
    while(i<arr.size()){
        int y = totalsum -arr[i];
        if (sol.find(y)!=sol.end()){
            vector<int> ans ={y,arr[i]};
            for (int i :ans){
                cout<<i<<endl;
            }
            break;
        }
        else{
            sol.insert(arr[i]);
        }
        i++;
    }
    return 0;
}