#include <iostream>

using namespace std;

int main() 
{
    int price;
    cin >> price;
    //cout << price << endl;
    int count = 0;

    int a = 500;
    int b = 100;
    int c = 50;
    int d = 10;
    int e = 5;
    int f = 1;

    int change = 1000 - price;

    count += (change / a);
    change -= a * (change / a);

    count += (change / b);
    change -= b * (change / b);

    count += (change / c);
    change -= c * (change / c);

    count += (change / d);
    change -= d * (change / d);

    count += (change / e);
    change -= e * (change / e);

    count += (change / f);
    change -= f * (change / f);

    cout << count << endl;

    return 0;
}