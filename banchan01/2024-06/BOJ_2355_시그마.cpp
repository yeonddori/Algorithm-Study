#include <iostream>
using namespace std;

long long a,b,result;
int main()
{
    cin >> a >>b;
    if (a<b)
        result = (b-a+1)*(a+b)/2;
    else
        result = (a-b+1)*(a+b)/2;

    cout <<result;
}