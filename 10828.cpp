#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    stack<int> s;
    int temp;
    int N;
    string str;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> str;
        if (str.compare("push") == 0) {
            cin >> temp;
            s.push(temp);
        } else if (str.compare("top") == 0) {
            if (s.empty()) {
                cout << "-1" << "\n";
            } else {
                cout << s.top() << "\n";
            }
        } else if (str.compare("size") == 0) {
            cout << s.size() << "\n";
        } else if (str.compare("pop") == 0) {
            if (s.empty()) {
                cout << "-1" << "\n";
            } else {
                cout << s.top() << "\n";
                s.pop();

            }
        } else if (str.compare("empty") == 0) {
            if (s.empty()) {
                cout << "1" << "\n";
            } else {
                cout << "0" << "\n";
            }
        }
    }
}