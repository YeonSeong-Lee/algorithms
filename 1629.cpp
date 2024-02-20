//  BOJ 1629 곱셈

#include <bits/stdc++.h>
using namespace std;

long long POW(long long a, long long b, long long c) {
  if (b == 0) return 1;
  if (b == 1) return a % c;
  long long val = POW(a, b / 2, c);
  val = val * val % c;
  if (b % 2 == 0) return val;
  return val * a % c;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  long long a, b, c;

  cin >> a >> b >> c;
  cout << POW(a, b, c);
}