#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int M, N, H;
int arr[100][100][100];
int dx[6] = {0, 0, 1, -1, 0, 0};
int dy[6] = {1, -1, 0, 0, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  cin >> M >> N >> H;

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < M; j++) {
      for (int k = 0; k < N; k++) {
        arr[i][j][k] = 1;
      }
    }
  }

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 10; k++) {
        cout << arr[i][j][k] << " ";
      }
      cout << "\n";
    }
  }
  
  

  cout << "WTF";
  
}


