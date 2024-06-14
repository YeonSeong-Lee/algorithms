#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    int arr[10'001] = {
        0,
    };
    cin.tie(0);
    cout.tie(0);

    int N;
    int temp;
    int max;
    cin >> N;
    while (N--)
    {
        cin >> temp;
        arr[temp] += 1;
    }
    for (int i = 0; i <= 10'000; i++)
    {
        for (int j = 0; j < arr[i]; j++)
        {
            cout << i << "\n";
        }
    }
}