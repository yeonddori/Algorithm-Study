#include <iostream>
#include <stack>
using namespace std;

string s;
int result= 0;
int tmp = 1;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> st;

    bool open = true;

    cin >> s;
    for(char ch :s)
    {
        if(ch=='(' || ch=='[')
        {
            st.push(ch);
            if(ch=='(')
            {
                tmp *= 2;
            }
            else
            {
                tmp *= 3;
            }
            open = true;
        }
        else if(!st.empty() && ch ==')')
        {
            if(st.top()== '(')
            {
                if(open)
                {
                    result += tmp;
                }
                st.pop();
                tmp /= 2;
            }
            else
            {
                result = 0;
                break;
            }
            open = false;
        }
        else if(!st.empty() && ch ==']')
        {
            if(st.top()=='[')
            {
                if(open)
                {
                    result += tmp;
                }
                st.pop();
                tmp /= 3;
            }
            else
            {
                result = 0;
                break;
            }
            open = false;
        }
        else if(st.empty() && (ch==')' || ch ==']'))
        {
            result = 0;
            break;
        }
    }
    if (!st.empty())
        result = 0;
    cout << result<<'\n';
}
