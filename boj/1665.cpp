#include <iostream>
#include <vector>

int K, N;

int main()
{
    using namespace std;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    vector<int> v;

    cin >> K >> N;
    unsigned int max = 0;
    while (K--)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
        if (temp > max)
        {
            max = temp;
        }
    }
    unsigned int start = 1;
    unsigned int end = max;
    unsigned int mid = (start + end) / 2;
    unsigned int ans = 0;
    while (start <= end)
    {
        mid = (start + end) / 2;
        unsigned int temp = 0;
        for (unsigned int i = 0; i < v.size(); i++)
        {
            temp += v[i] / mid;
        }
        if (temp >= N)
        {
            start = mid + 1;
            if (ans < mid) {
               ans = mid;
            }
        }
        else
        {
            end = mid - 1;
        }
      
    }
    cout << ans;
}