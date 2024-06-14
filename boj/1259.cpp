#include <iostream>
#include <string>

using namespace std;

string isPalindrome(string str) {
    for (int i = 0; i < str.length() / 2; i++) {
        if (str[i] != str[str.length() - i -1]) {
            return "no";
        }
    }
    return "yes";
}

int main() {

    string temp;
    cin >> temp;
    while(temp.compare("0") != 0)
    {
        cout << isPalindrome(temp) << "\n";
        cin >> temp;
    }

}