#include <iostream>

using namespace std;

int main()
{
    int i, j, n, m, f = 0, r = 0, c = 0, result;
    char a[50][50];

    cin >> n >> m;

    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            cin >> a[i][j];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            if (a[i][j] == 'X')
                f = 1;
        if (f == 0) r++;
        f = 0;
    }

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
            if (a[j][i] == 'X')
                f = 1;
        if (f == 0) c++;
        f = 0;
    }

    result = (r > c) ? r : c;

    cout << result << endl;
}
