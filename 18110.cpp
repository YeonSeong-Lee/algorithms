#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

vector<int> v;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  
  int K;
  cin >> K;

  while (K--)
  {
    int temp;
    cin >> temp;
    v.push_back(temp); 
  }
  int drop = 0;
  double ans = 0;
  double cnt = 0;
  if (!v.empty()){
    drop = round(v.size() * 0.15);
  }
  sort(v.begin(), v.end());
  for (int i = 0; i < v.size(); i++) {
    if (i < drop || i > v.size() -1 - drop) {
      continue;
    }
    ans += v[i];
    cnt += 1;
  }
  if (cnt == 0) {
    cout << 0;
    return 0;
  }
  cout << round(ans / cnt);
}