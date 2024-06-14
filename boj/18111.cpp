#include <iostream>
#include <vector>
using namespace std;

vector<int> v;
int ans_time = __INT_MAX__;
int ans_height;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int M, N, B;
    cin >> M >> N >> B;

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int temp;
            cin >> temp;
            v.push_back(temp);
        }
    }
    // 땅의 높이를 기준으로 브루트포스 탐색
    for (int current_height = 0; current_height <= 256; current_height++)
    {
        int during_time = 0;
        int minus_block = 0;
        int plus_block = 0;
        for (int i = 0; i < M * N; i++)
        {
            int temp_height = v[i];
            if (temp_height > current_height)
            {
                minus_block += temp_height - current_height;
            }
            if (temp_height < current_height)
            {
                plus_block += current_height - temp_height;
            }
        }
        during_time += 2 * minus_block + plus_block;
        if (B + minus_block >= plus_block && during_time <= ans_time)
        {
            ans_time = during_time;
            ans_height = current_height;
        }
    }
    cout << ans_time << " " << ans_height;
}