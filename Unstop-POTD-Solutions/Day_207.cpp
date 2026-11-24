#include <bits/stdc++.h>
using namespace std;

struct Sighting {
    long long time;
    int id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    cin >> n >> W;

    vector<int> cnt(200001, 0);
    deque<Sighting> dq;

    set<pair<int, int>> active;

    for (int i = 0; i < n; i++) {
        char type;
        long long t;
        cin >> type >> t;

        while (!dq.empty() && dq.front().time <= t - W) {
            int id = dq.front().id;
            dq.pop_front();

            active.erase({-cnt[id], id});
            cnt[id]--;

            if (cnt[id] > 0) {
                active.insert({-cnt[id], id});
            }
        }

        if (type == 'S') {
            int id;
            cin >> id;

            if (cnt[id] > 0) {
                active.erase({-cnt[id], id});
            }

            cnt[id]++;
            active.insert({-cnt[id], id});

            dq.push_back({t, id});
        }
        else {
            if (active.empty()) {
                cout << "QUIET\n";
            } else {
                auto it = *active.begin();
                cout << it.second << " " << -it.first << "\n";
            }
        }
    }

    return 0;
}