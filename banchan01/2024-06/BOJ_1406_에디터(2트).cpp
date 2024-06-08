#include <iostream>
#include <list>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string word;
    cin >> word;

    list<int> lst;
    for(auto ch : word)
        lst.push_back(ch);

    list<int>::iterator cursor = lst.end();

    int n;
    cin >> n;

    while(n--)
    {
        char ch;
        cin >> ch;
        if (ch=='P')
        {
            char ch2;
            cin >> ch2;
            lst.insert(cursor,ch2);
        }
        else if(ch == 'L')
        {
            if(cursor!=lst.begin())
                cursor--;
        }
        else if(ch=='D')
        {
            if(cursor!=lst.end())
                cursor++;
        }
        else if(ch=='B')
        {
            if(cursor!=lst.begin())
            {
                cursor--;
                cursor = lst.erase(cursor);
            }
        }
    }

    for(char ch : lst)
    {
        cout << ch;
    }
    return 0;

    // 역시 저번 풀이는 너무 아이디어성이 강했음..ㅋ
    // 스택 2개를 붙여서 커서 조정하는건 너무 발상인듯
    // 연결리스트로 푸는게 훨 나음
}