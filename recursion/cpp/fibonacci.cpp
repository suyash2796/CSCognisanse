#include<iostream>
using namespace std;

int fibonacci(int n);

//O(2^n) solution..
int fibonacci(int n){
    if (n==1)
        return 0;
    else if(n==2)
        return 1;
    else
        return fibonacci(n-1)+fibonacci(n-2);
}

//ToDO - O(N) solution using memoization
//use unordered set for memoization

int main(){
    int n=10;
    cout<< fibonacci(n)<<endl;
}