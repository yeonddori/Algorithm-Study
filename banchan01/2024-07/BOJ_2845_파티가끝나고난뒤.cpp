#include <iostream>
using namespace std;

int main()
{
    int l,p;
    cin >> l >>p;

    int arr[5];
    for(int i=0; i<5; i++)
    {
        cin >> arr[i];
    }

    for(int i=0 ;i<5; i++)
    {
        cout << arr[i] - l*p<< ' ';
    }
}
