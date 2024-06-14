#include <bits/stdc++.h>
using namespace std;


int M, N, H;
int dx[6] = {0, 0, 1, -1, 0, 0};
int dy[6] = {1, -1, 0, 0, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};

int board[103][103][103];
int dist[103][103][103];
queue<tuple<int,int,int>> Q;


int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  cin >> M >> N >> H;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
        cin >> board[i][j][k];
        if (board[i][j][k] == 1) {
          Q.push({i, j, k});
        }
        if (board[i][j][k] == 0) {
          dist[i][j][k] = -1;
        }
      }
    }
  }

  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    int curX, curY, curZ;
    tie(curZ, curY, curX) = cur;

    for (int dir = 0; dir < 6; dir++) {
      int nx = curX + dx[dir];
      int ny = curY + dy[dir];
      int nz = curZ + dz[dir];
      if (nx < 0 || ny < 0 || nz < 0 || nx >= M || ny >= N || nz >= H) {
        continue;
      }
      if (dist[nz][ny][nx] >= 0) {
        continue;
      }
      dist[nz][ny][nx] = dist[curZ][curY][curX] + 1;
      Q.push({nz,ny,nx});
    }
  }

  int ans = 0;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
        if (dist[i][j][k] == -1) {
          cout << -1 << "\n";
          return 0;
        }
        ans = max(ans, dist[i][j][k]);
      }
    }
  }
  cout << ans << "\n";
  return 0;
}
