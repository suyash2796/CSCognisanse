#include<vector>
using namespace std;
int second_min(vector<int> arr){
    int n = arr.size();
    int first = INT8_MAX;
    int second =  INT8_MAX;
    for (int i=0;i<=n;i++){
        if (arr[i]<first){
            second =  first;
            first = arr[i];
        }
        else if (second>arr[i] && arr[i]!=first){
            second = arr[i];
        }
    }
    return second;
}
