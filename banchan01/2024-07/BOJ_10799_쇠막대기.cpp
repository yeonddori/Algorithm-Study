#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int result = 0;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    bool is_laser = true;

    stack<int> st;

    // �� ������ �������� ������ ���� �����ϴ� ����
    vector<int> vc(50000,0);

    for(char ch : s)
    {
        if (ch=='(')
        {
            st.push(ch);
            is_laser = true;
        }
        else
        {
            // ������ �϶�
            if(is_laser)
            {
                is_laser = false;
                st.pop();
                for(int i =0; i<st.size(); i++)
                {
                    vc[i] += 1;
                }
            }
            // ����� �϶�
            else
            {
                result += vc[st.size()-1] + 1;
                vc[st.size()-1] = 0;
                st.pop();
            }
        }
    }
    cout << result;
}
