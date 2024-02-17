// BOJ 1697 숨박꼭질

#include <bits/stdc++.h>
using namespace std;

int N, K;
const int MAX = 100000;
int board[MAX + 1];
queue<int> Q;


int main() {{
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> K;
  fill(board, board + MAX + 1, -1);
  Q.push(N);
  board[N] = 0;

  while (board[K] == -1) {
    int cur = Q.front(); Q.pop();
    for (int next : { cur - 1, cur + 1, 2 * cur}) {
      if (next < 0 || next > MAX + 1) {
        continue;
      }
      if (board[next] != -1) {
        continue;
      }
      board[next] = board[cur] + 1;
      Q.push(next);
    }
  }
  cout << board[K];
}}