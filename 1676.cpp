#include <iostream>
using namespace std;

int main() {
    int N;
    string f;
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    cout << N / 5 + N / 25 + N / 125;

    return 0;
}