#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<array<long long, 3>> jobs(n);

    for (auto &job : jobs)
        cin >> job[0] >> job[1] >> job[2];

    sort(jobs.begin(), jobs.end(), [](const auto &a, const auto &b) {
        return a[1] < b[1];
    });

    vector<long long> ends(n);
    for (int i = 0; i < n; ++i)
        ends[i] = jobs[i][1];

    vector<long long> dp(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        long long start = jobs[i - 1][0];
        long long profit = jobs[i - 1][2];

        int j = upper_bound(ends.begin(), ends.begin() + i - 1, start) - ends.begin();

        dp[i] = max(dp[i - 1], dp[j] + profit);
    }

    cout << dp[n] << '\n';

    return 0;
}