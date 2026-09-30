#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 1e9 + 7;

string toOctal(long long num) {
    if (num == 0) return "0";

    string octal = "";
    while (num > 0) {
        octal = char((num % 8) + '0') + octal;
        num /= 8;
    }
    return octal;
}

string user_logic(int N) {
    /*
    Vowels:
    0 -> a
    1 -> e
    2 -> i
    3 -> o
    4 -> u
    */

    if (N == 0)
        return "1";

    // Base case: length 1
    vector<long long> dp(5, 1);

    for (int len = 2; len <= N; len++) {
        vector<long long> ndp(5, 0);

        // Current vowel transitions
        ndp[0] = (dp[1] + dp[4]) % MOD; // a <- e,u
        ndp[1] = (dp[0] + dp[2]) % MOD; // e <- a,i
        ndp[2] = (dp[1] + dp[3]) % MOD; // i <- e,o
        ndp[3] = (dp[2] + dp[4]) % MOD; // o <- i,u
        ndp[4] = (dp[0] + dp[3]) % MOD; // u <- a,o

        dp = ndp;
    }

    long long total = 0;
    for (long long x : dp) {
        total = (total + x) % MOD;
    }

    // If no valid strings
    if (total == 0)
        return "1";

    // Convert to octal
    return toOctal(total);
}

int main() {
    int N;
    cin >> N;

    string result = user_logic(N);
    cout << result << endl;

    return 0;
}