#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int arr[10];
queue<pair<int, int>> Q;

bool isExistMoreImport(int curr)
{
    bool res = false;
    for (int i = 9; i > curr; i--)
    {
        if (arr[i] > 0)
        {
            res = true;
            break;
        }
    }
    return res;
}

int main()
{
    int num_of_test_case;
    int ans = 0;
    cin >> num_of_test_case;

    while (num_of_test_case--)
    {
        int N, M;
        fill(arr, arr + 10, 0);
        Q = queue<pair<int, int>>();
        cin >> N >> M;
        for (int i = 0; i < N; i++)
        {
            int temp;
            cin >> temp;
            arr[temp]++;
            Q.push({temp, i});
        }
        int cnt = 1;
        while (!Q.empty())
        {
            if (isExistMoreImport(Q.front().first))
            {
                Q.push(Q.front());
                Q.pop();
            }
            else if (Q.front().second == M)
            {
                cout << cnt << "\n";
                break;
            }
            else
            {
                arr[Q.front().first]--;
                Q.pop();
                cnt++;
            }
        }
    }
    return 0;
}