#include <iostream>
#include <algorithm>
using namespace std;

int n;
int result = 0;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >>n;
    int* arr = new int[n];

    // 다솜이꺼는 배열에 안넣고 따로 저장
    int dasom;
    cin >> dasom;

    for(int i =0; i<n-1; i++)
    {
        cin >> arr[i];
    }

    while(1)
    {
        int mmaaxx = 0;
        int max_idx = 0;

        // max 값 찾기
        for(int i =0; i<n-1; i++)
        {
            if(mmaaxx < arr[i])
            {
                mmaaxx = arr[i];
                max_idx = i;
            }
        }

        if (dasom > mmaaxx)
        {
            cout << result;
            break;
        }

        dasom++;
        arr[max_idx]--;
        result++;
    }
    delete []arr;
    return 0;
}