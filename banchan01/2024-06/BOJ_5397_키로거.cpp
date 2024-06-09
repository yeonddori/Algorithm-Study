#include <iostream>
#include <list>
using namespace std;

int n;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    while(n--)
    {
        string passwd;
        cin >> passwd;

        list<char> answer;
        list<char>::iterator cursor = answer.begin();

        for(char ch : passwd)
        {
            if (ch=='<')
            {
                if (cursor!=answer.begin())
                    cursor--;
            }
            else if(ch=='>')
            {
                if (cursor!=answer.end())
                    cursor++;
            }
            else if (ch =='-')
            {
                if (cursor!=answer.begin())
                {
                    cursor--;
                    cursor = answer.erase(cursor);
                }
            }
            else if(ch-'A'>=0 && ch-'Z'<=0)
            {
                cursor = answer.insert(cursor,ch);
                cursor++;
            }
            else if(ch-'a'>=0 && ch-'z'<=0)
            {
                cursor = answer.insert(cursor,ch);
                cursor++;
            }
            else if(ch>='0' && ch<='9')
            {
                cursor = answer.insert(cursor,ch);
                cursor++;
            }
            else
                break;
        }

        for(char ch : answer)
        {
            cout << ch;
        }
        cout << '\n';
    }
    return 0;
}