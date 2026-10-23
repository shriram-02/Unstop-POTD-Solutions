
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Batch {
    ll expiry;
    ll remaining;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll Z;
    cin >> N >> Z;

    // Min-heap: {expiry day, batch number}
    priority_queue<
        pair<ll, ll>,
        vector<pair<ll, ll>>,
        greater<pair<ll, ll>>
    > pq;

    // Batch number -> batch information
    unordered_map<ll, Batch> batches;

    ll expired = 0;
    ll recalled = 0;

    while (N--) {
        ll day;
        char type;
        cin >> day >> type;

        // Step 1: Expire batches before processing this entry.
        while (!pq.empty() && pq.top().first < day) {
            auto [expiry, id] = pq.top();
            pq.pop();

            Batch &b = batches[id];

            if (b.remaining > 0) {
                expired += b.remaining;
                b.remaining = 0;
            }
        }

        // Step 2: Process the current log entry.
        if (type == 'R') {
            ll B, E, Q;
            cin >> B >> E >> Q;

            batches[B] = {E, Q};
            pq.push({E, B});
        }
        else if (type == 'D') {
            ll Q;
            cin >> Q;

            ll supplied = 0;

            while (Q > 0 && !pq.empty()) {
                auto [expiry, id] = pq.top();
                pq.pop();

                Batch &b = batches[id];

                // Skip empty or previously recalled batches.
                if (b.remaining == 0) {
                    continue;
                }

                ll take = min(Q, b.remaining);

                Q -= take;
                supplied += take;
                b.remaining -= take;

                // Keep this batch available if doses remain.
                if (b.remaining > 0) {
                    pq.push({expiry, id});
                }
            }

            cout << supplied << '\n';
        }
        else if (type == 'C') {
            ll B;
            cin >> B;

            auto it = batches.find(B);

            if (it != batches.end() &&
                it->second.remaining > 0) {
                recalled += it->second.remaining;
                it->second.remaining = 0;
            }
        }
    }

    // Step 3: Audit on day Z.
    while (!pq.empty() && pq.top().first < Z) {
        auto [expiry, id] = pq.top();
        pq.pop();

        Batch &b = batches[id];

        if (b.remaining > 0) {
            expired += b.remaining;
            b.remaining = 0;
        }
    }

    cout << "EXPIRED " << expired
         << " RECALLED " << recalled << '\n';

    return 0;
}