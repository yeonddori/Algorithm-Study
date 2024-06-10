#include <iostream>
#include <queue>

using namespace std;

int n,k;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >>n >> k;

    queue<int> q;

    for(int i=1; i<n+1; i++)
    {
        q.push(i);
    }

    cout << '<';

    while(q.size())
    {
        for(int i=1; i<k;i++)
        {
            q.push(q.front());
            q.pop();
        }
        cout << q.front();
        q.pop();

        if(q.size())
        {
            cout << ", ";
        }
    }
    cout << '>';
    return 0;
}
