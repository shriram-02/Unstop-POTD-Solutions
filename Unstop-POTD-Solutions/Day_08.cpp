#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <climits>
#include <unordered_set>

using namespace std;

typedef long long ll;
const ll INF = 1e18;

struct Edge {
    int to, wt;
};

struct State {
    ll dist;
    int node;
    int mode; // 0 = Road, 1 = Rail

    bool operator>(const State &other) const {
        return dist > other.dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<Edge>> road(n), rail(n);

    int r;
    cin >> r;

    for (int i = 0; i < r; i++) {
        int u, v, t;
        cin >> u >> v >> t;

        road[u].push_back({v, t});
        road[v].push_back({u, t});
    }

    int s;
    cin >> s;

    for (int i = 0; i < s; i++) {
        int u, v, t;
        cin >> u >> v >> t;

        rail[u].push_back({v, t});
        rail[v].push_back({u, t});
    }

    int m;
    cin >> m;

    unordered_set<int> intermodal;

    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        intermodal.insert(x);
    }

    int transferTime, src, dst;
    cin >> transferTime >> src >> dst;

    // dist[node][mode]
    vector<vector<ll>> dist(n, vector<ll>(2, INF));

    priority_queue<State, vector<State>, greater<State>> pq;

    // Start with Road mode if possible
    dist[src][0] = 0;
    pq.push({0, src, 0});

    // Start with Rail mode if possible
    dist[src][1] = 0;
    pq.push({0, src, 1});

    while (!pq.empty()) {
        State cur = pq.top();
        pq.pop();

        ll d = cur.dist;
        int u = cur.node;
        int mode = cur.mode;

        if (d > dist[u][mode]) continue;

        // Move within same mode
        if (mode == 0) {
            for (auto &e : road[u]) {
                int v = e.to;
                ll nd = d + e.wt;

                if (nd < dist[v][0]) {
                    dist[v][0] = nd;
                    pq.push({nd, v, 0});
                }
            }
        } else {
            for (auto &e : rail[u]) {
                int v = e.to;
                ll nd = d + e.wt;

                if (nd < dist[v][1]) {
                    dist[v][1] = nd;
                    pq.push({nd, v, 1});
                }
            }
        }

        // Transfer mode at intermodal hub
        if (intermodal.count(u)) {
            int newMode = 1 - mode;
            ll nd = d + transferTime;

            if (nd < dist[u][newMode]) {
                dist[u][newMode] = nd;
                pq.push({nd, u, newMode});
            }
        }
    }

    ll ans = min(dist[dst][0], dist[dst][1]);

    if (ans == INF)
        cout << -1 << '\n';
    else
        cout << ans << '\n';

    return 0;
}