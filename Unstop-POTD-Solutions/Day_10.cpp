#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <deque>

using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string line;
    if (!getline(cin, line)) return 0;
    while (line.empty() && getline(cin, line));

    stringstream ss(line);
    ll val;
    vector<ll> fun_factors;
    while (ss >> val) {
        fun_factors.push_back(val);
    }

    int K, M;
    if (!(cin >> K >> M)) return 0;

    int N = (int)fun_factors.size();
    if (N == 0) {
        cout << 0 << endl;
        return 0;
    }

    vector<ll> S(N + 1, 0);
    for (int i = 0; i < N; ++i) {
        S[i + 1] = S[i] + fun_factors[i];
    }

    vector<ll> dp(N);
    vector<ll> W(N);
    deque<int> dq_dp; 
    deque<int> dq_W; 

    const ll LLINF = 2e18;

    for (int i = 0; i < N; ++i) {

        if (i >= 2) {
            while (!dq_dp.empty() && dp[dq_dp.back()] <= dp[i - 2]) {
                dq_dp.pop_back();
            }
            dq_dp.push_back(i - 2);
        }
        while (!dq_dp.empty() && dq_dp.front() < i - K - 1) {
            dq_dp.pop_front();
        }


        ll base_i = -LLINF;
        if (i <= K) { 
            base_i = 0;
        }
        if (!dq_dp.empty()) {
            base_i = max(base_i, dp[dq_dp.front()]);
        }


        W[i] = base_i - S[i];
        while (!dq_W.empty() && W[dq_W.back()] <= W[i]) {
            dq_W.pop_back();
        }
        dq_W.push_back(i);
        while (!dq_W.empty() && dq_W.front() < i - M + 1) {
            dq_W.pop_front();
        }

        dp[i] = S[i + 1] + W[dq_W.front()];
    }


    ll ans = (N <= K) ? 0 : -LLINF;


    for (int i = max(0, N - K - 1); i < N; ++i) {
        if (dp[i] > ans) {
            ans = dp[i];
        }
    }

    cout << ans << endl;

    return 0;
}