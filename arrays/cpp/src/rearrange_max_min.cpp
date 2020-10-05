/* Write a C++ program to rearrange a given sorted array of positive integers . Go to the editor
Note: In final array, first element should be maximum value, second minimum value, third second maximum value , fourth second minimum value, fifth third maximum and so on.
*/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> arr={1,2,3,4,2,5,8,1};
    vector<int> res(arr.size(),0);

    //sorting array of positive integers
    sort(arr.begin(), arr.end());
    int max = arr.size()-1;
    int min  = 0;
    int result=true;

    for(int i=0;i<arr.size();i++){
        if (result)
            res[i] = arr[max--];
        else
            res[i] = arr[min++];
 
        result = !result;
    }
    for (auto i: res) cout<<i<<',';
    return 0;
}