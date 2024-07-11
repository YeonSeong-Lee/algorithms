#include <iostream>
using namespace std;

// 로직이 맞는지 확인용.

typedef long long ll;
ll s, x, d;

int main() 
{
	int n;
	cin >> n;
	while (n--)
	{
		scanf("%lld %lld",&s,&x);
		if ((s - x) & 1) {
			cout << 0 << endl;
			continue;
		}

		d = (s - x) / 2;
		ll res = 1;

		for (ll i = 0; i <= 57; i++) {
			ll bit = (1LL << i);
			if (d & bit) {
				if (x & bit) {
					res = 0;
					break;
				}
			}
			else {
				if (x & bit)
					res *= 2LL;
			}
		}
		printf("%lld\n",res);
	}
}
