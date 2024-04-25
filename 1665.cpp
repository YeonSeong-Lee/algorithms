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
    int max = 0;
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
    int start = 1;
    int end = max;
    int mid = (start + end) / 2;
    while (start < mid)
    {
        cout << "start " << start << " " << "mid " << mid << " end " << end << "\n";
        int temp = 0;
        for (int i = 0; i < v.size(); i++)
        {
            temp += v[i] / mid;
            cout << "temp :" << temp << " v[i] / mid " << v[i] / mid << "\n";
        }
        if (temp > N)
        {
            start = mid;
        }
        else
        {
            end = mid;
        }
        mid = (start + end) / 2;
    }
    cout << mid;
}