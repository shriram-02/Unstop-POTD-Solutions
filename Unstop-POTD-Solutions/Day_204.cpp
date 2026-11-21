#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long T;
    cin >> N >> T;

    vector<int> ans(N);
    unordered_map<long long, int> freq;
    queue<pair<long long, long long>> q;

    int distinct = 0;
    int maxDistinct = 0;
    long long earliestMinute = 0;

    for (int i = 0; i < N; i++) {
        long long minute, badge;
        cin >> minute >> badge;

        while (!q.empty() && q.front().first < minute - T + 1) {
            long long oldBadge = q.front().second;
            q.pop();

            freq[oldBadge]--;

            if (freq[oldBadge] == 0) {
                freq.erase(oldBadge);
                distinct--;
            }
        }

        q.push({minute, badge});

        if (freq[badge] == 0) {
            distinct++;
        }

        freq[badge]++;

        ans[i] = distinct;

        if (distinct > maxDistinct) {
            maxDistinct = distinct;
            earliestMinute = minute;
        }
    }

    cout << maxDistinct << " " << earliestMinute << "\n";

    for (int i = 0; i < N; i++) {
        cout << ans[i];
        if (i < N - 1) cout << " ";
    }

    cout << "\n";

    return 0;
}