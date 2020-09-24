#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
#include<vector>
using std::vector;
using std::sort;

int main(){
    vector<int> A={-5,-2,3,6,8};
    vector<int> temp;
    for(int i=0;i<A.size();i++){
        temp.push_back(pow(A[i],2));
    }
    sort(temp.begin(), temp.end());
    cout<<"sorted array with squares: \n";
    for(auto item: temp){
        cout<<item<<"\n";
    }
    return 0;
}