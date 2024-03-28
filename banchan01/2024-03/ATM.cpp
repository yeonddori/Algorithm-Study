#include <iostream>

using namespace std;

int find_max(int arr[], int len)
{
    int max = arr[0];
    for (int i = 0; i < len; i++)
    {
        if (arr[i] >= max)
        {
            max = arr[i];
        }
    }
    return max;
}

void counting_sort(int arr[], int len, int MAX)
{
    int* temp = new int[MAX + 1]();

    for(int i=0;i<len;i++)
    {
        for(int j=1;j<MAX+1;j++)
        {
            if(arr[i] == j)
            {
                temp[j] += 1;
                arr[i] = 0;
            }
        }
    }
    int cnt =0;
    int idx = 0;
    for(int i=1; i<MAX+1; i++)
    {
        if(temp[i] != 0)
        {
            while(cnt != temp[i])
            {
                arr[idx++] =i;
                cnt++;
            }
            cnt = 0;
        }
    }

    delete[] temp;
}

int main()
{
    int n;
    cin >> n;

    int* time = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> time[i];
    }

    int MAX = find_max(time, n);
    counting_sort(time, n, MAX);

    int result =0;

    for(int i=0;i<n;i++)
    {
        for(int j=0; j <= i; j++)
        {
            result += time[j];
        }
    }
    cout <<result<<endl;

    delete[] time;
    return 0;
}