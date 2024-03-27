#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K;
    int loop = 0;
    vector<int> v;

    cin >> N >> K;

    for (int i = 0; i < N; i++){
        v.push_back(i + 1);
    }
    while (!v.empty()) {
        loop++;
        int idx = (loop * K) % v.size();
        cout << "idx: " << idx << '\n';
        v.erase(v.begin() + idx);
    }
}