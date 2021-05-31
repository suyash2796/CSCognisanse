#include<iostream>
#include<vector>
using namespace std;

int maxSumSubarray(vector<int> array);

int maxSumSubarray(vector<int> array){
    int maxSoFar = array[0];
    int maxEndHere = array[0];
    for(int i=1;i<array.size();i++){
        int num = array[i];
        maxEndHere = max(num,  maxEndHere+num);
        maxSoFar = max(maxEndHere, maxSoFar);
    }
    return maxSoFar;
}

int main(){
    vector<int> array = {1,2,-1,3,5,-9,-2};
    int max_num = maxSumSubarray(array);
    cout<<"Maximum sum obtained from sub array - "<<max_num <<endl;
    return 0;
}