#include <iostream>
#include <stack>
using namespace std;

int main()
{
    int K;
    int temp;
    stack<int> S;
    int sum = 0;

    cin >> K;

    while (K--)
    {
        cin >> temp;
        if (temp == 0)
        {
            sum -= S.top();
            S.pop();
        }
        else
        {
            sum += temp;
            S.push(temp);
        }
    }
    cout << sum;
}