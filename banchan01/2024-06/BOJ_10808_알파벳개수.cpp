#include <iostream>

using namespace std;

// ������ �����ϸ� �ڵ����� 0���� �ʱ�ȭ��.
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