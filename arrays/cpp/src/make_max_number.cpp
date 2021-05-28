//cpp program to form largest number from array of strings

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#include "../utils/utils.h"
 
void makeLargest(vector<string> arr) 
{ 
    sort(arr.begin(), arr.end(), Compare); 
  
    for (int i=0; i < arr.size() ; i++ ) 
        cout << arr[i]; 
} 
 //driver function
int main()
{
    vector<string> arr = {"2", "1", "25", "3", "4"};
    int n = arr.size();
    makeLargest(arr);
 
   return 0;
}