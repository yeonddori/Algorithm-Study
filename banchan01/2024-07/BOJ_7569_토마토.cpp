#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>

using namespace std;

int m,n,h;
int tomato[105][105][105];
int dis[105][105][105];

int dx[6] = {1,0,0,-1,0,0};
int dy[6] = {0,1,0,0,-1,0};
int dz[6] = {0,0,1,0,0,-1};
bool all_ripe = true;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> m >>n >>h;
    queue<tuple<int,int,int>> Q;

    for(int k=0; k<h; k++)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                dis[k][i][j] = -1;
            }
        }
    }

    for(int k=0; k<h; k++)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                cin >> tomato[k][i][j];
                if(tomato[k][i][j] == 1)
                {
                    Q.push({k,i,j});
                    dis[k][i][j]++;
                }
                if(tomato[k][i][j] == 0)
                {
                    all_ripe = false;
                }
            }
        }
    }
    if(all_ripe)
    {
        cout << 0;
        return 0;
    }
    while(!Q.empty())
    {
        tuple<int,int,int> cur = Q.front();
        Q.pop();

        for(int i=0; i<6; i++)
        {
            int nx = get<1>(cur) + dx[i];
            int ny = get<2>(cur) + dy[i];
            int nz = get<0>(cur) + dz[i];
            if(nx<0 || nx>=n || ny<0 || ny>=m || nz<0 || nz>=h)
                continue;
            if(tomato[nz][nx][ny] != 0 || dis[nz][nx][ny] != -1)
                continue;
            dis[nz][nx][ny] = dis[get<0>(cur)][get<1>(cur)][get<2>(cur)] + 1;
            Q.push({nz,nx,ny});
        }
    }
    int result =0;
    for(int k=0; k<h; k++)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if (dis[k][i][j] == -1 && tomato[k][i][j] != -1)
                {
                    cout <<-1;
                    return 0;
                }
                result = max(result, dis[k][i][j]);
            }
        }
    }
    cout <<result;
}
