#include <iostream>
#include <queue>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int n;
  queue<int> Q;
  int temp;
  string op;

  cin >> n;

  for (int i = 0; i < n; i++) {

  cin >> op;

  if (op.compare("push") == 0) {
    cin >> temp;
    Q.push(temp);
  } else if (op.compare("pop") == 0) {
    if (Q.empty()) {
      cout << -1 << "\n";
    } else {
      cout << Q.front() << "\n";
      Q.pop();
    }
  } else if (op.compare("size") == 0) {
      cout << Q.size() << "\n";
  } else if (op.compare("empty") == 0) {
    cout << (Q.empty() ? 1 : 0)<< "\n";
  } else if (op.compare("front") == 0) {
    cout << (Q.empty() ? -1 : Q.front()) << "\n";
  } else { 
    cout << (Q.empty() ? -1 : Q.back()) << "\n";
  }
  }
  return 0;
}