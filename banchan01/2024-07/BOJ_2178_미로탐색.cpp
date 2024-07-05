#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>

#define X first
#define Y second

using namespace std;

char miro[105][105];
int dis[105][105];
int n,m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    // 미로 배열에 채워넣기
    cin >> n >> m;
    string s;
    for(int i=0; i<n; i++)
    {
        int j = 0;
        cin >> s;
        for(char ch : s)
        {
            miro[i][j++] = ch;
        }
    }

    for(int i=0; i<n; i++)
    {
        fill(dis[i],dis[i]+m, -1);
    }

    queue<pair<int,int>> Q;
    Q.push({0,0});
    dis[0][0] += 1;

    while(!Q.empty())
    {
        pair<int,int> cur = Q.front();
        Q.pop();
        for(int i=0; i<4; i++)
        {
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if(dis[nx][ny] != -1 || miro[nx][ny] != '1')
                continue;
            dis[nx][ny] = dis[cur.X][cur.Y] + 1;
            Q.push({nx,ny});
        }
    }
    cout << dis[n-1][m-1] + 1;
}
