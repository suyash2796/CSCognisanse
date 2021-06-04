#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    string str = "ababababbabbbababa";
    string substr = "abbax";
    vector<int> pattern(substr.size(), -1);
    int pl = 0;
    int pr=1;
    while(pr< substr.size()){
        if (substr[pr]==substr[pl]){
            pattern[pr] = pl;
            pr++;
            pl++;
        }
        else if(pl>0)
            pl=pattern[pl-1]+1;
        else
        {
            pr++;
        }
        
    }
    int i=0;
    int j=0;
    while (i+substr.size()-j <= str.size())
    {
        if (substr[j]==str[i]){
            if (j==substr.size()-1){
                cout<<"substring matched"<<endl;
                return 0;}
            i++;
            j++;

        }
        else if (j>0)
            j = pattern[j-1] +1;
        else
            i++;
    }
    cout<<"substring not matched"<<endl;
    return 0;
}