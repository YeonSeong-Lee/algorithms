#include <iostream>
#include <deque>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n;
  deque<int> deque;
  int temp;
  string op;

  cin >> n;

  for (int i = 0; i < n; i++) {

  cin >> op;

  if (op.compare("push_back") == 0) {
    cin >> temp;
    deque.push_back(temp);
  } else if (op.compare("push_front") == 0) {
    cin >> temp;
    deque.push_front(temp);
  } 
  else if (op.compare("pop_front") == 0) {
    if (deque.empty()) {
      cout << -1 << "\n";
    } else {
      cout << deque.front() << "\n";
      deque.pop_front();
    }
  } else if (op.compare("pop_back") == 0) {
    if (deque.empty()) {
      cout << -1 << "\n";
    } else {
      cout << deque.back() << "\n";
      deque.pop_back();
    }
  }
   else if (op.compare("size") == 0) {
      cout << deque.size() << "\n";
  } else if (op.compare("empty") == 0) {
    cout << (deque.empty() ? 1 : 0)<< "\n";
  } else if (op.compare("front") == 0) {
    cout << (deque.empty() ? -1 : deque.front()) << "\n";
  } else { 
    cout << (deque.empty() ? -1 : deque.back()) << "\n";
  }
  }
  return 0;
}