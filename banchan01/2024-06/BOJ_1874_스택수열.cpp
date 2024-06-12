#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >>n;

    // 주어진 수열 채우기
    vector<int> vc;
    for(int i=0; i<n;i++)
    {
        int a;
        cin >> a;
        vc.push_back(a);
    }

    int order = 1;
    stack<int> st;
    vector<string> result;
    for(int i=0;i<n;i++)
    {
        if (vc[i] >= order)
        {
            while(order<=vc[i])
            {
                st.push(order);
                result.push_back("+");
                order++;
            }
            st.pop();
            result.push_back("-");
        }

        else
        {
            if(st.top() == vc[i])
            {
                st.pop();
                result.push_back("-");
            }
            else
            {
                result.clear();
                result.push_back("NO");
                break;
            }
        }
    }
    for(string ch : result)
    {
        cout << ch <<'\n';
    }
    return 0;
}