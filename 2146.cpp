#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int N;
    vector<int> v;
    cin >> N;
    for (int i = 0; i < N; i++) {
        v.push_back(i + 1);
    }
    while (v.size() > 1)
    {
        v.erase(v.begin());
        v.push_back(*v.begin());
        v.erase(v.begin());
    }
    cout << v.front();
    return 0;
}