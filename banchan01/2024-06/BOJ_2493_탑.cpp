#include <iostream>
#include <stack>
#include <utility>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    stack<pair<int,int>> st;
    st.push({100000001,0});

    int h;
    for(int i=1; i<=n; i++)
    {
        cin >> h;
        while(!st.empty())
        {
            if (h<=st.top().first)
            {
                cout << st.top().second << ' ';
                break;
            }
            else
            {
                st.pop();
            }
        }
        st.push(make_pair(h,i));
    }
}