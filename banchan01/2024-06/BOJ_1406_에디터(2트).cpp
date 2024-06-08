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

    // ���� ���� Ǯ�̴� �ʹ� ���̵��� ������..��
    // ���� 2���� �ٿ��� Ŀ�� �����ϴ°� �ʹ� �߻��ε�
    // ���Ḯ��Ʈ�� Ǫ�°� �� ����
}