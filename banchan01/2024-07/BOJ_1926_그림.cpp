#include <iostream>
#include <queue>
#include <utility>
#define X first
#define Y second

using namespace std;

int picture[505][505];
bool visited[505][505];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int n,m;
int picture_num = 0;
int max_area = -1;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<pair<int,int>> Q;

    //그림 입력받기
    cin >> n >> m;
    for(int i =0; i<n;i++)
    {
        for(int j=0; j<m; j++)
        {
            cin >> picture[i][j];
        }
    }

    for(int row = 0; row<n; row++)
    {
        for(int col=0; col<m; col++)
        {
            int area = 0;
            if(picture[row][col] == 1 && !visited[row][col])
            {
                picture_num++;
                visited[row][col] = 1;
                Q.push({row,col});
            }

            while(!Q.empty())
            {
                pair<int,int> cur = Q.front();
                Q.pop();
                area++;
                for(int i=0; i<4; i++)
                {
                    int nx = cur.X + dx[i];
                    int ny = cur.Y + dy[i];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= m)
                        continue;
                    if(visited[nx][ny] || picture[nx][ny] != 1)
                        continue;
                    visited[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
            if (area > max_area)
            {
                max_area = area;
            }

        }
    }
    cout << picture_num<<'\n'<< max_area;
}
