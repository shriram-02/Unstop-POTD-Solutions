
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q, G;
    cin >> q >> G;

    // Min heap for every blood group
    vector<priority_queue<
        pair<int, int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>
    >> pq(G + 1);

    // Tracks whether a unit is available
    unordered_map<int, bool> active;
    active.reserve(q);

    for (int i = 0; i < q; i++) {
        int t;
        char type;
        cin >> t >> type;

        if (type == 'D') {
            int id, group, expiry;
            cin >> id >> group >> expiry;

            pq[group].push({expiry, id});
            active[id] = true;
        }

        else if (type == 'C') {
            int id;
            cin >> id;

            // Withdraw the unit
            active[id] = false;
        }

        else if (type == 'R') {
            int group;
            cin >> group;

            auto &heap = pq[group];

            // Remove withdrawn or expired units
            while (!heap.empty()) {
                auto [expiry, id] = heap.top();

                if (!active[id] || expiry < t) {
                    active[id] = false;
                    heap.pop();
                }
                else {
                    break;
                }
            }

            // Give the best available unit
            if (heap.empty()) {
                cout << "NONE\n";
            }
            else {
                auto [expiry, id] = heap.top();
                heap.pop();

                active[id] = false;

                cout << id << "\n";
            }
        }
    }

    return 0;
}
