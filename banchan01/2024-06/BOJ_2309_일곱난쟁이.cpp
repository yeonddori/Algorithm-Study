#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> numbers(9);
    for(int i=0; i<9; i++)
    {
        cin >> numbers[i];
    }
    int sum = accumulate(numbers.begin(),numbers.end(),0);
    int residue = sum - 100;

    bool found = false;

    for(int i=0; i<9 && !found ;i++)
    {
        for(int j=i+1; j<9; j++)
        {
            if (numbers[i] + numbers[j] == residue)
            {
                numbers[i] = -1;
                numbers[j] = -1;
                found = true;
                break;
            }
        }
    }
    sort(numbers.begin(),numbers.end());

    for(int num:numbers)
    {
        if(num>0)
        {
            cout <<num<<'\n';
        }
    }

    return 0;
}