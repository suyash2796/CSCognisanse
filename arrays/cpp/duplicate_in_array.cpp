#include<iostream>
#include<vector>
using std::vector;
using namespace std;
using std::cout;

int main () {
    vector<int>A={1,2,3,4,3};
    int n=A.size();
    vector<int>nav(n-1,0);
    int i=0;
    while(i<n){
        if(nav[A[i]-1]==0) nav[A[i]-1]=1;
        else {
            cout<<A[i];
            return A[i];
        }
        i++;
    }
   return -1;
}