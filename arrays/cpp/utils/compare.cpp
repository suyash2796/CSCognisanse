#include<string>
using namespace std;

int Compare(string X, string Y)
{
    // append Y at the end of X
    string XY = X.append(Y);
 
    // append X at the end of Y
    string YX = Y.append(X);
    // cehc if XY is greater or YX
   if (XY > YX)
   {
     return 1;
   }
   else
   {
     return 0;
   }
    
}