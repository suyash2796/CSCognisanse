#include<iostream>
#include<vector>
using namespace std;

int main() 
{
    vector<int> A= {1,2,2,3,2};
    int c=0;
    vector<int> preDif;
    vector<int> postDif(A.size(),0);
    int val=0;
    for(int i=0;i<A.size();i++){
        if(i%2==0) val+=A[i];
        else val-=A[i];
        preDif.push_back(val);
    }
    val=0;
    for(int i=A.size()-1;i>=0;i--){
        if(i%2==0) val+=A[i];
        else val-=A[i];
        postDif[i]=val;
    }
    for(int i=0;i<A.size();i++){
        if(preDif[i]==postDif[i]) c++;
    }
    cout<<"answer:"<<c;
    return 0;
}