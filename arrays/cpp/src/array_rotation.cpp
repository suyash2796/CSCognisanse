#include<iostream>
#include<vector>
using namespace std;
int main () {
    vector<int> arr ={1,2,3,4,5,6,7};
    int nu_of_rotation=8;
	vector<int> rotated; 
	int size = arr.size();

	for (int i = 0; i < arr.size(); i++) {
		rotated.push_back(arr[(i + nu_of_rotation)%size]);
	}
    for(auto item:rotated){
        cout<<item<<",";
    }
    cout<<"\n";
	return 0; 
}