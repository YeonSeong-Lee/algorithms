#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int N, M;
    int temp;
    unordered_map<int, int> cards;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        if (cards.find(temp) != std::end(cards)) {
            cards[temp] = cards[temp] + 1;
        }
        cards.insert({temp, 1});
    }
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> temp;
        if (cards.find(temp) != std::end(cards)) {
            cout << cards[temp] << " ";
        } else {
            cout << 0 << " ";
        }
    }
    return 0;
}