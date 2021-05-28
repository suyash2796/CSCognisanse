#include <iostream> 
#include <vector> 
#include <algorithm> 
using namespace std; 
using std::partial_sort;

int main() 
{ 
    vector<int> v;
    int n;
    cout<<"enter number of elements of verctor"<<"\n";
    cin>>n;
    for(int i=0;i<n;i++){
        int p;
        cin>>p;
        v.push_back(p);
    }
    cout<<"below are the elements of vector\n";
    for(auto i:v){
        cout<<i<<endl;
    }
    partial_sort(v.begin(), v.begin() + 5, v.end()); 
  
    // Displaying the vector after applying partial_sort 
    // for (ip = v.begin(); ip != v.end(); ++ip) { 
    //     cout << *ip << " "; 
    // } 
    cout<<"elements after partial sort"<<"\n";
    //below is range based access of vector elements
    // for(auto i:v){
    //     cout<<i<<endl;
    // }

    //below is simple access based on vector size
    for(int i=0;i<v.size();i++){
        cout<<v[i];
    }
    return 0; 
} 