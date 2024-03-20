#include <iostream>
#include <string>

using namespace std;
int N;
int tempSum;
int total;
string arr;

int main() {
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> arr;
        tempSum = 0;
        total = 0;
        for (int j = 0; j < arr.length(); j ++) {
            if (arr[j] == 'O') {
                tempSum++;
                total += tempSum;
            }
            if (arr[j] == 'X') {
                tempSum = 0;
            }
            cout << "tempSum " << tempSum << "\n";
        }
        cout << total << "\n";
    }
}