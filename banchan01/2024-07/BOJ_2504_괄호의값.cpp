#include <iostream>
#include <stack>
using namespace std;

string s;
int result= 0;
int tmp = 1;
int main()
{
    stack<int> st;

    bool close = false;

    cin >> s;
    for(char ch :s)
    {
        if(ch=='(' || ch == '[')
        {
            if (close)
            {
                result += tmp;
            }

            st.push(ch);
            close = false;
            tmp = 1;
        }
        else if(ch==')')
        {
            if(!st.empty() && st.top()=='(')
            {
                st.pop();
                tmp *= 2;
            }
            else
            {
                cout << 0;
                break;
            }
            close = true;
        }

        else if(ch==']')
        {
            else if(!st.empty() && st.top()=='[')
            {
                st.pop();
                tmp *= 3;
            }
            else
            {
                cout << 0;
                break;
            }
            close = true;
        }
    }
}
