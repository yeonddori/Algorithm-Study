#include <iostream>
#include <queue>

using namespace std;

int n;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<int> Q;
    cin >> n;
    string command;

    while(n--)
    {
        cin >> command;
        if (command == "push")
        {
            int num;
            cin >> num;
            Q.push(num);
        }
        else if (command == "pop")
        {
            if (!Q.empty())
            {
                cout << Q.front() << '\n';
                Q.pop();
            }
            else
                cout << -1<<'\n';
        }
        else if (command == "size")
        {
            cout << Q.size()<< '\n';
        }
        else if (command == "empty")
        {
            cout << Q.empty()<< '\n';
        }
        else if (command == "front")
        {
            if (!Q.empty())
            {
                cout << Q.front()<< '\n';
            }
            else
                cout << -1<< '\n';
        }
        else if (command == "back")
        {
            if (!Q.empty())
            {
                cout << Q.back()<< '\n';
            }
            else
                cout << -1<< '\n';
        }
    }
}