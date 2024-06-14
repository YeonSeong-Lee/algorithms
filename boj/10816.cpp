#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    int temp;
    unordered_map<int, int> cards;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        cards[temp] = cards[temp] + 1;
    }
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> temp;
        cout << cards[temp] << " ";
    }
    return 0;
}