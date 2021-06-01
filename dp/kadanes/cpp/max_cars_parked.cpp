#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int maxCarsParked(vector<vector<int>> array);

int maxCarsParked(vector<vector<int>> array){
    int array_size = 2*(array.size());
    vector< pair <int,bool> > parkingRegister(array_size,{0,true});
    

    for (int i = 0; i < array.size(); i++) {
        parkingRegister[2 * i] = { array[i][0], true };
        parkingRegister[2 * i + 1] = { array[i][1], false };
    }

    sort(parkingRegister.begin(), parkingRegister.end());

    int curMax=0;
    int finalMax=0;

    for (int i=0; i<array_size;++i){
        if (parkingRegister[i].second)
            curMax++;
        else{
            if (curMax > finalMax) 
                finalMax = curMax;
   
            curMax--;
        }
    }

    return finalMax;
}

int main(){

    vector<vector<int>> arr= { { 1012, 1136 },
        { 1017, 1412 },
        { 1015, 1620 } };
    
    cout<<"max cars parked ->"<< maxCarsParked(arr)<<endl;
    return 0;
}