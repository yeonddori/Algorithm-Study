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
        // �Է¹ޱ�
        string s;
        getline(cin,s);

        // ��������
        if(s == ".")
            break;

        // ��ȣ ���ÿ� �ְ�, �����
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
