#include<iostream>
using namespace std;

int main(){
    string main_str="abaabbbaaa";
    string sub_str = "suy";
    int l_main= main_str.length();
    int l_sub= sub_str.length();
    bool matched= false;
    for (int i=0;i<=l_main-l_sub+1;i++){
        int cnt=0;
        for(int j=0;j<=l_sub;j++){
            if(main_str[i+j]!=sub_str[j]){
                break;
            }
            cnt++;
        }
        if(cnt==l_sub){
            matched=true;
        }
    }
    if (matched==true){
        cout<<"sub string matched!";
    }
    else{
        cout<<"sub string not matched!";
    }
    return 0;
}