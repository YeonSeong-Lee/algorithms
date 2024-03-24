// BOJ 4179 불!
#include <bits/stdc++.h>
using namespace std;

int R, C;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
string board[1000];
int escapeDist[1000][1000];
int fireDist[1000][1000];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> R >> C;
  for (int i = 0; i < R; i ++) {
    fill(escapeDist[i], escapeDist[i] + C, -1);
    fill(fireDist[i], fireDist[i] + C, -1);
  }

  for (int i = 0; i < R; i++) {
      cin >> board[i];
  }
  queue<pair<int, int>> escapeQ;  
  queue<pair<int, int>> fireQ;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (board[i][wj] == 'J') {
        escapeQ.push({i, j});
        escapeDist[i][j] = 0;
      }
      if (board[i][j] == 'F') {
        fireQ.push({i, j});
        fireDist[i][j] = 0;
      }
    }
  }
  while (!fireQ.empty()) {
    auto cur = fireQ.front();
    fireQ.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.second + dx[i];
      int ny  = cur.first + dy[i];
      if (nx < 0 || ny < 0 || nx >= C || ny >= R) {
        continue;
      }
      if (fireDist[ny][nx] >= 0 || board[ny][nx] == '#') {
        continue;
      }
      fireDist[ny][nx] = fireDist[cur.first][cur.second] + 1;
      fireQ.push({ny, nx});
    }
  }

  while (!escapeQ.empty()) {
    auto cur = escapeQ.front();
    escapeQ.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.second + dx[i];
      int ny = cur.first + dy[i];
      if (nx <  0 || ny < 0 || nx >= C || ny >= R) {
        cout << escapeDist[cur.first][cur.second] + 1;
        return 0;
      }
      if (escapeDist[ny][nx] >= 0 || board[ny][nx] == '#') {
        continue;
      }
      if (fireDist[ny][nx] != -1 && fireDist[ny][nx] <= escapeDist[cur.first][cur.second] + 1) {
        continue;
      }
      escapeDist[ny][nx] = escapeDist[cur.first][cur.second] + 1;
      escapeQ.push({ny, nx}); 
    }
  }
  cout << "IMPOSSIBLE";
}
