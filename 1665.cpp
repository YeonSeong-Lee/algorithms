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
    }
}