#include<iostream>
#include<vector>
using namespace std;
#include "../utils/utils.h"
int main() {
vector<int> A = {1,2,4,1,6,25,1,2};
vector<int> arr;
int flag;

for(int i=0;i<A.size();i++){
    flag=0;
    for(int j=i+1;j< A.size();j++){
        if (A[i]<A[j]){
            flag=1;
            break;
        }
    }
    if (flag==0)
        arr.push_back(A[i]);
}
print_int_arr(arr);
return 0;
}
