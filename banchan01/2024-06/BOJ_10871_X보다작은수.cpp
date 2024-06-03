#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,x;
    cin >> n >> x;
    int arr[n];
    for(int i=0; i<n; i++)
    {
        int a;
        cin >> a;
        arr[i] = a;
    }

    for(int i=0; i<n; i++)
    {
        if (arr[i]<x)
        {
            cout << arr[i]<<" ";
        }
    }
    return 0;
}