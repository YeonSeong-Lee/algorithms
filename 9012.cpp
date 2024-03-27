#include <iostream>
#include <stack>
#include <string>

using namespace std;

string isVPS(string s) {
    stack<char> stack;
    
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            stack.push('(');
        } else if (s[i] == ')') {
            if (stack.empty()) {
                return "NO";
            }
            stack.pop();
        }
    }

    return stack.size() == 0 ? "YES" : "NO";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int T;
    string s;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> s;
        cout << isVPS(s) << "\n";
    }

}