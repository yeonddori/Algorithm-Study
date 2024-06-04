#include <iostream>

using namespace std;

// 전역에 선언하면 자동으로 0으로 초기화됨.
int arr[26];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string word;
    cin >> word;

    for(char n:word)
    {
        arr[n-'a'] += 1;
    }
    for(int i = 0; i < 26; i++)
    {
        cout << arr[i]<<" ";
    }
    return 0;
}