#include <iostream>
#include <sstream>
#include <deque>
#define LEN 100005
using namespace std;

int T;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> T;
    for(int i =0; i<T; ++i)
    {
        bool rvs = false, err = false;

        deque<int> dq;

        string cm;
        cin >> cm;

        int num;
        cin >> num;

        string arr_shape;
        cin >> arr_shape;

        //대괄호 제거
        arr_shape = arr_shape.substr(1, arr_shape.size() - 2);
        //콤마 제거
        stringstream ss(arr_shape);
        string temp;

        while(getline(ss,temp,','))
        {
            dq.push_back(stoi(temp));
        }

        for(auto ch : cm)
        {
            if (ch == 'R')
            {
                if (rvs)
                    rvs = false;
                else
                    rvs = true;
            }
            else if(ch == 'D')
            {
                if(!dq.empty())
                {
                    if (!rvs)
                    {
                        dq.pop_front();
                    }
                    else
                        dq.pop_back();
                }
                else
                {
                    cout << "error";
                    err = true;
                    break;
                }
            }
        }
        //출력

        if(!dq.empty())
        {
            cout<< '[';

            if (rvs==false)
            {
                for(auto it = dq.begin(); it != dq.end(); ++it)
                {
                    if(it!= dq.end()-1)
                    {
                        cout << *it << ',';
                    }
                    else
                        cout << *it;
                }
            }
            else
            {
                for(auto it = dq.end()-1; it != dq.begin()-1; --it)
                {
                    if(it!= dq.begin())
                    {
                        cout << *it << ',';
                    }
                    else
                        cout << *it;
                }
            }
            cout << ']';
        }
        else
            cout<<"[]";

        cout << '\n';
    }
    return 0;
}
