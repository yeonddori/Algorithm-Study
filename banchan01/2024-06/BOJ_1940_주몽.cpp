#include <iostream>
#include <vector>
#define SIZE 15000

using namespace std;

int n,m;
int arr[SIZE];

int main()
{
    cin >> n >> m;

    for(int i=0;i<n;i++)
    {
        cin >> arr[i];
    }

    int result = 0;
    for(int i=0; i<n; i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if (arr[i] + arr[j] == m)
                result++;
        }
    }

    cout << result;
    return 0;
}
