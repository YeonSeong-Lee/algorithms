#include <iostream>
#include <set>
using namespace std;

int main() {
    int N;
    int temp;
    set<int> s;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        s.insert(temp);
    }
    for (auto iter = s.begin(); iter != s.end(); iter++) {
        cout << *iter << "\n";
    }
}