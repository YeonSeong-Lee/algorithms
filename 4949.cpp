//  BOJ 4949 균형잡힌 세상

#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (1) {
    string s;
    getline(cin, s);
    if (s == ".") break;
    stack<char> st;
    bool flag = true;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '(' || s[i] == '[')
        st.push(s[i]);
      else if (s[i] == ')') {
        if (st.empty() || st.top() != '(') {
          flag = false;
          break;
        }
        st.pop();
      } else if (s[i] == ']') {
        if (st.empty() || st.top() != '[') {
          flag = false;
          break;
        }
        st.pop();
      }
    }
    if (!st.empty()) flag = false;
    if (flag)
      cout << "yes\n";
    else
      cout << "no\n";
  }
  return 0;
}