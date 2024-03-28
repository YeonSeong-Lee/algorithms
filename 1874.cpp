#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  stack<int> S;
  vector<char> ans;
  int temp;
  int iter = 1;
  int N;
  cin >> N;
  while (N--) {
    cin >> temp;
    while (iter <= temp) {
      S.push(iter);
      ans.push_back('+');
      iter++;
    }
    if (temp == S.top()) {
        S.pop();
        ans.push_back('-');
    } else {
      cout << "NO";
      return 0;
    }
  }
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i] << "\n";
  }
}