#include <iostream>
#include <algorithm>
#define SIZE 1000005
using namespace std;

bool Eratos[SIZE];

void make_chae();
void verify(int num);

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    // 체를 1로 초기화 시켜뻐리기
    fill(Eratos,Eratos+SIZE,true);
    make_chae();

    int n=1;
    while(cin >> n)
    {
        if(n==0) break;
        verify(n);
    }
    return 0;
}

void make_chae()
{
    for(int i=2; i*i<=SIZE; i++)
    {
        if(Eratos[i])
        {
            for(int j=i*i; j<=SIZE; j+=i)
            {
                Eratos[j] = false;
            }
        }
    }
}

void verify(int num)
{
    for(int i = num-3; i>=3; i-=2)
    {
        if(Eratos[i] && Eratos[num-i])
        {
            cout << num << " = " << num-i << " + " << i << '\n';
            return;
        }
    }
    cout << "Goldbach's conjecture is wrong." << '\n';
}