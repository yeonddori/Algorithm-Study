#include <iostream>
#include <stack>
using namespace std;

int n;
int result= 0;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    while(n--)
    {
        int n_A = 0;
        int n_B = 0;
        stack<int> st;

        string goodword;
        cin >> goodword;

        for(char ch : goodword)
        {
            if (ch == 'A' && n_A == 0)
            {
                st.push(ch);
                n_A++;
            }
            else if(ch=='B' && n_B == 0)
            {
                st.push(ch);
                n_B++;
            }
            else if(ch=='A'&& n_A != 0)
            {
                if (st.top()=='A')
                {
                    st.pop();
                    n_A--;
                }
                else
                {
                    st.push(ch);
                    n_A++;
                }

            }
            else if(ch=='B' && n_B != 0)
            {
                if(st.top()=='B')
                {
                    st.pop();
                    n_B--;
                }
                else
                {
                    st.push(ch);
                    n_B++;
                }
            }
        }
        if (st.empty())
            result++;
    }
    cout << result;
}
