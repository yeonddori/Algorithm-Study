#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

using namespace std;

int n,m;
int result;
int main()
{
    cin >> n >> m;
    int start = 0;
    deque<int> dq;
    for(int i=1; i<=n; ++i)
    {
        dq.push_back(i);
    }

    vector<int> index;
    for(int i=0; i<m; ++i)
    {
        int num;
        cin >> num;
        index.push_back(num);
    }
    int vc_idx = 0;

    while(vc_idx != m)
    {

        if (dq.front() == index[vc_idx])
        {
            dq.pop_front();
            n--;
            vc_idx++;
            continue;
        }

        auto it = find(dq.begin(), dq.end(), index[vc_idx]);
        int dst = distance(dq.begin(), it);

        if (dst<= n/2)
        {
            dq.push_back(dq.front());
            dq.pop_front();
            result++;
        }
        else
        {
            dq.push_front(dq.back());
            dq.pop_back();
            result++;
        }
    }
    cout << result;
}
