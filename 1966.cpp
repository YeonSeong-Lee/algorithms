#include <iostream>
#include <queue>
using namespace std;


int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int N;
  queue<<int,int>> Q;

  cin >> N;
  while (N--) {
    int queue_num;
    int index;
    int cnt = 0;
    cin >> queue_num >> index;
    for (int i = 0; i < queue_num; i++) {
      int temp; 
      cin >> temp;
      Q.push({temp, i});
    }
  }
  return 0;
}