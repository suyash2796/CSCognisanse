#include<iostream>
#include<vector>
#include "../utils/utils.h"
using namespace std;


int main() {
    vector<int> A ={1,2,-1,4,5,6,-7};
    long long sum=0;
    long long ans = INT8_MIN;
    vector<int>fin;
    vector<int>temp;
    for(auto i:A){
        if(i<0){
            sum=0;
	    temp.clear();
            continue;
        }
        sum+=i;
        temp.push_back(i);
        if(ans<sum or (ans==sum and fin.size()<temp.size())){
            ans=sum;
            fin = temp;
        }
    }
    print_int_arr(fin);

    return 0;
}
