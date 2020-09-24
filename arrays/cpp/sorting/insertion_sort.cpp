#include<iostream>
#include<vector>
using namespace std;
using std::cin;
using std::cout;
using std::vector;

void insertion_sort(vector<int> arr, int size);

int main(){
    vector<int> arr;
    cout<<"enter the number of elements of array\n";
    int n;
    cin>>n;
    cout<<"enter the elements of array\n";
    for (int i=0;i<n;i++){
        int j;
        cin>>j;
        arr.push_back(j);
    }
    cout<<"entered arr is: ";
    for(int i=0;i<n;i++){
        cout<<arr[i];
    }
    insertion_sort(arr,n);
}
void insertion_sort(vector<int> arr, int size){
    int i=0;
    int j=0;
    int key;
    for(int i=1;i<size;i++){
        key = arr[i];
        j = i-1;
        while(key<arr[j] && j>=0){
            arr[j+1] = arr[j];
            j=j-1;
        }
        arr[j+1] = key;

    }
    cout<<"\nsorted array using insertion sort: ";
    for (int i=0;i<arr.size();i++){
        cout<<arr[i];
    }
    cout<<"\n";
}