#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>

#define X first
#define Y second
using namespace std;

int tomato[1005][1005];
int dis[1005][1005];
int dx[4] ={1,0,-1,0};
int dy[4] = {0,1,0,-1};

int m,n;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<pair<int,int>> Q;
    cin >> m >> n;

    for(int i=0; i<n; i++)
    {
        fill(dis[i], dis[i]+m, -1);
    }

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            cin >> tomato[i][j];
            if (tomato[i][j] == 1)
            {
                dis[i][j]++;
                Q.push({i,j});
            }

        }
    }

    while(!Q.empty())
    {
        pair<int,int> cur = Q.front();
        Q.pop();

        for(int i=0 ;i<4; i++)
        {
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];
            if(nx<0 || nx>= n ||ny <0 ||ny>=m)
                continue;
            if(tomato[nx][ny] != 0 || dis[nx][ny] != -1)
                continue;
            dis[nx][ny] = dis[cur.X][cur.Y] + 1;
            Q.push({nx,ny});
        }
    }

    int result = 0;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m;j++)
        {
            if(tomato[i][j] == 0 && dis[i][j] == -1)
            {
                cout << -1;
                return 0;
            }
            result = max(result, dis[i][j]);
        }
    }
    cout << result;
}