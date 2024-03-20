#include <iostream>

using namespace std;

int temp;
bool isAscending;
bool isDecending;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    isAscending = true;
    isDecending = true;

    for (int i = 0; i < 8; i++) {
        cin >> temp;

        if (temp != i + 1) {
            isAscending = false;
        }
        if (temp != 8 - i) {
            isDecending = false;
        }
    }
    if (isAscending == true) {
        return "ascending";
    }
    if (isDecending == true) {
        return "descending"
    }
    return "mixed"
}