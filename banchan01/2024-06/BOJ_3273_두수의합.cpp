#include <iostream>
using namespace std;

int arr[2000005] = {};
int n,x;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i =0; i<n; i++)
    {
        int a;
        cin >> a;
        arr[a] = 1;
    }

    cin >> x;
    int result = 0;

    for(int i=1; i<x; i++)
    {
        if (arr[i] == 1 && arr[x-i] == 1)
        {
            result += 1;
        }
    }
    cout << result/2;
    return 0;
}