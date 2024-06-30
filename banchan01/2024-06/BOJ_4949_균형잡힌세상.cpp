#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    while(1)
    {
        bool flag = true;
        stack<int> st;
        // 입력받기
        string s;
        getline(cin,s);

        // 종료조건
        if(s == ".")
            break;

        // 괄호 스택에 넣고, 지우기
        for(char ch : s)
        {
            if(ch=='(' || ch=='[')
            {
                st.push(ch);
            }

            else if(ch==')')
            {
                if(st.empty() || st.top()!='(')
                {
                    flag = false;
                    break;
                }
                st.pop();
            }
            else if(ch==']')
            {
                if(st.empty() || st.top()!='[')
                {
                    flag = false;
                    break;
                }
                st.pop();
            }
            
        }
        if(!st.empty())
            flag = false;
        if(flag)
            cout << "yes" << '\n';
        else
            cout << "no" << '\n';
                
    }
}
