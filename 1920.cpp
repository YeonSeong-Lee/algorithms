#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
  int N, M;
  int temp;
	unordered_map<int, bool> A;
  cin >> N;
  for (int i = 0; i < N; i++) {
		int temp;
    cin >> temp;
		A.insert({temp, true});
  }
  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> temp;
    if (A.find(temp) != A.end()) {
      cout << 1 << "\n";
    }
    else {
      cout << 0 << "\n";
    }
  }
  
  return 0;
}