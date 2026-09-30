#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 1000000007;

long long factorial(int n) {
    long long res = 1;
    for (int i = 2; i <= n; i++) {
        res = (res * i) % MOD;
    }
    return res;
}

int countPrimes(int n) {
    vector<bool> prime(n + 1, true);

    prime[0] = prime[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                prime[j] = false;
            }
        }
    }

    int cnt = 0;

    for (int i = 2; i <= n; i++) {
        if (prime[i]) cnt++;
    }

    return cnt;
}

int main() {
    int n;
    cin >> n;

    int primes = countPrimes(n);

    long long ans =
        (factorial(primes) * factorial(n - primes)) % MOD;

    cout << ans << endl;

    return 0;
}