#include <iostream>
using namespace std;

int n;
string word1;
string word2;
string result;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i=0; i<n; i++)
    {
        char arr[26] ={0};
        result = "Possible";

        cin >> word1;
        for(auto unit : word1)
        {
            arr[unit -'a']++;
        }

        cin >> word2;
        for(auto unit : word2)
        {
            arr[unit -'a']--;
        }

        for(auto i : arr)
        {
            if (i != 0)
            {
                result = "Impossible";
            }
        }
        cout << result << '\n';
    }
    return 0;
}
