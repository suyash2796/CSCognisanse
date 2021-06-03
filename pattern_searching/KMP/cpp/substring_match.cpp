#include<iostream>
#include<vector>
#include<algorithm>



int main(){
    string str = 'ababababbabbbababa';
    string substr = 'abba';
    vector<int> pattern(substr.size(), -1);
    int pl = 0;
    int pr=1;
    while(pr< substr.size()){
        if (substr[pr]==substr[pl]){
            pattern[pr] = pl;
            pr++;
            pj++;
        }
        else if(pl>0)
            pl=pattern[pl-1]+1;
        else
        {
            pr++;
        }
        
    }
//todo
    //implement match loop
    return 0;
}