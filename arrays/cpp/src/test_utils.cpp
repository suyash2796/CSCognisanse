#include<iostream>
#include<vector>
using namespace std;
#include "../utils/utils.h"

/* this is main function to test 
utility functions defined under utils 
folder. Utils.h header having the declartion
of util functions*/


int main(){
    vector<int> arr={1,4,5,2,3,1};
    int a=2;
    int b=3;
    merge_sort(arr, 0,6);
    //arr = insertion_sort(arr,6);
    // arr = selection_sort(arr,6);
    print_int_arr(arr);
    // swap(&a,&b);
    // cout<<a;
    // cout<<b;
    // cout<<max(a,b);
    // cout<<min(a,b);
    return 0;
}
