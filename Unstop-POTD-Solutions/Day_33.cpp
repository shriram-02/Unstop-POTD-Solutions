#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <climits>

using namespace std;

struct Edge {
    int to, cost, bm, flip;
};

int starlight_jumps(int N, int M, int K, vector<int>& bits,
                    vector<tuple<int, int, int, int, int>>& edges) {
    
    int startMask = 0;
    for (int b : bits) startMask |= (1 << b);

    vector<vector<Edge>> adj(N + 1);

    for (auto &e : edges) {
        int u, v, cost, bm, flip;
        tie(u, v, cost, bm, flip) = e;
        adj[u].push_back({v, cost, bm, flip});
    }

    const long long INF = LLONG_MAX / 4;
    const int MASKS = 1024;

    vector<long long> dist((N + 1) * MASKS, INF);

    auto id = [&](int node, int mask) {
        return node * MASKS + mask;
    };

    priority_queue<
        pair<long long, pair<int,int>>,
        vector<pair<long long, pair<int,int>>>,
        greater<pair<long long, pair<int,int>>>
    > pq;

    dist[id(1, startMask)] = 0;
    pq.push({0, {1, startMask}});

    while (!pq.empty()) {
        auto cur = pq.top();
        pq.pop();

        long long d = cur.first;
        int u = cur.second.first;
        int mask = cur.second.second;

        if (d != dist[id(u, mask)]) continue;

        if (u == N && mask == startMask)
            return (int)d;

        for (const auto &e : adj[u]) {
            if ((mask & e.bm) != e.bm) continue;

            int newMask = mask ^ e.flip;
            long long nd = d + e.cost;

            int idx = id(e.to, newMask);

            if (nd < dist[idx]) {
                dist[idx] = nd;
                pq.push({nd, {e.to, newMask}});
            }
        }
    }

    return -1;
}

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    vector<int> bits(K);
    for (int i = 0; i < K; i++) cin >> bits[i];

    vector<tuple<int, int, int, int, int>> edges(M);

    for (int i = 0; i < M; i++) {
        int u, v, cost, bm, flip_mask;
        cin >> u >> v >> cost >> bm >> flip_mask;
        edges[i] = {u, v, cost, bm, flip_mask};
    }

    cout << starlight_jumps(N, M, K, bits, edges) << '\n';
    return 0;
}