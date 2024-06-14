#include <iostream>
#include <queue>
<<<<<<< HEAD
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
=======
using namespace std;


int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int N;
  queue<<int,int>> Q;

  cin >> N;
  while (N--) {
    int queue_num;
    int index;
    int cnt = 0;
    cin >> queue_num >> index;
    for (int i = 0; i < queue_num; i++) {
      int temp; 
      cin >> temp;
      Q.push({temp, i});
    }
  }
  return 0;
>>>>>>> 07db686d06b7c48ad56a70572731d476ce5f45b3
}