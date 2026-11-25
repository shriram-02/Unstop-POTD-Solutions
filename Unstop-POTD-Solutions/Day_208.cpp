
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll INF = (1LL << 60);

// Segment Tree
struct SegmentTree {
    int n;
    vector<ll> tree;

    SegmentTree(int sz) {
        n = sz;
        tree.assign(4 * n + 5, INF);
    }

    // Activate a waiting aircraft
    void update(int node, int start, int end,
                int idx, ll val) {

        if (start == end) {
            tree[node] = val;
            return;
        }

        int mid = (start + end) / 2;

        if (idx <= mid)
            update(node * 2, start, mid, idx, val);
        else
            update(node * 2 + 1, mid + 1, end, idx, val);

        tree[node] = min(tree[node * 2],
                         tree[node * 2 + 1]);
    }

    void update(int idx, ll val) {
        update(1, 1, n, idx, val);
    }

    // Find the earliest waiting aircraft
    // whose wingspan is <= gate limit.
    int findFirst(int node, int start, int end,
                  ll limit) {

        if (tree[node] > limit)
            return -1;

        if (start == end)
            return start;

        int mid = (start + end) / 2;

        // Search left side first to get
        // the earliest aircraft.
        if (tree[node * 2] <= limit) {
            return findFirst(node * 2,
                             start, mid, limit);
        }

        return findFirst(node * 2 + 1,
                         mid + 1, end, limit);
    }

    int findFirst(ll limit) {
        if (tree[1] > limit)
            return -1;

        return findFirst(1, 1, n, limit);
    }
};

struct Aircraft {
    ll arrival;
    ll wingspan;
    ll duration;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int g, n;
    cin >> g >> n;

    // Idle gates: {wingspan limit, gate number}
    set<pair<ll, int>> idle;

    vector<ll> gateLimit(g + 1);

    for (int i = 1; i <= g; i++) {
        cin >> gateLimit[i];
        idle.insert({gateLimit[i], i});
    }

    vector<Aircraft> planes(n + 1);

    for (int i = 1; i <= n; i++) {
        cin >> planes[i].arrival
            >> planes[i].wingspan
            >> planes[i].duration;
    }

    // Segment tree for waiting aircraft
    SegmentTree seg(n);

    // {release time, gate number}
    using Event = pair<ll, int>;

    priority_queue<
        Event,
        vector<Event>,
        greater<Event>
    > pq;

    vector<int> answer(n + 1);

    ll totalWait = 0;
    ll lastDeparture = 0;

    // Assign an aircraft to a gate
    auto dock = [&](int plane, int gate, ll time) {

        answer[plane] = gate;

        totalWait += time - planes[plane].arrival;

        ll departure = time + planes[plane].duration;

        lastDeparture = max(lastDeparture, departure);

        pq.push({departure, gate});
    };

    // Process all gate releases up to time t
    auto processReleases = [&](ll t) {

        while (!pq.empty() && pq.top().first <= t) {

            auto [releaseTime, gate] = pq.top();
            pq.pop();

            // Find earliest waiting aircraft
            // that fits this released gate.
            int plane = seg.findFirst(gateLimit[gate]);

            if (plane != -1) {

                // Remove aircraft from waiting list
                seg.update(plane, INF);

                // Assign it immediately
                dock(plane, gate, releaseTime);

            } else {

                // No waiting aircraft fits
                // Gate becomes idle.
                idle.insert({gateLimit[gate], gate});
            }
        }
    };

    // Process aircraft in input order
    for (int i = 1; i <= n; i++) {

        ll arrival = planes[i].arrival;
        ll w = planes[i].wingspan;

        // Releases happen before arrivals
        // at the same moment.
        processReleases(arrival);

        // Find the narrowest suitable idle gate
        auto it = idle.lower_bound({w, 0});

        if (it != idle.end()) {

            int gate = it->second;

            idle.erase(it);

            dock(i, gate, arrival);

        } else {

            // No idle gate available.
            // Aircraft enters holding pattern.
            seg.update(i, w);
        }
    }

    // Process all remaining releases.
    // This also docks any aircraft still waiting.
    while (!pq.empty()) {

        auto [releaseTime, gate] = pq.top();
        pq.pop();

        int plane = seg.findFirst(gateLimit[gate]);

        if (plane != -1) {

            seg.update(plane, INF);

            dock(plane, gate, releaseTime);

        } else {

            idle.insert({gateLimit[gate], gate});
        }
    }

    cout << totalWait << " " << lastDeparture << "\n";

    for (int i = 1; i <= n; i++) {
        cout << answer[i];

        if (i < n)
            cout << " ";
    }

    cout << "\n";

    return 0;
}