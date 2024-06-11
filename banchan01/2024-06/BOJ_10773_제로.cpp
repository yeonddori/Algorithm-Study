#include <iostream>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> st;
    int k;
    cin >> k;

    int n;

    int result = 0;
    while(k--)
    {
        cin >> n;
        if (n!=0)
        {
            st.push(n);
            result += n;
        }
        else
        {
            if (st.size())
            {
                result -= st.top();
                st.pop();
            }
        }
    }
    cout << result;
}