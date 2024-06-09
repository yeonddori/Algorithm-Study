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
                answer.insert(cursor,ch);
            }
            else if(ch-'a'>=0 && ch-'z'<=0)
            {
                answer.insert(cursor,ch);
            }
            else if(ch>='0' && ch<='9')
            {
                answer.insert(cursor,ch);
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

// insert는 실행 후, iterator가 자동으로 원래 자기자리를 가리킴
// erase 는 실행 후, iterator가 어딜 가리킬지 모름... 따라서 꼭 return 값을 받아서 iterator를 update 해줘야함.
// erase의 return 값 ==  지워진 요소 다음 요소의 iterator