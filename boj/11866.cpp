#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K;
    vector<int> v;

    cin >> N >> K;

    for (int i = 0; i < N; i++){
        v.push_back(i + 1);
    }
    cout << "<";
    int idx = K - 1;
    while (!v.empty()) {
        cout << v[idx];
        v.erase(v.begin() + idx);
        if (v.empty()) break;
        idx = (idx + K - 1) % v.size();
        cout << ", ";
    }
    cout << ">";
}