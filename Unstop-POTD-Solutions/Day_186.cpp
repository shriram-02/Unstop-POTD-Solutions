#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Query {
    int id;
    int t;
    int a;
};

struct Edge {
    int u, v;
};

struct RollbackDSU {
    vector<int> parent;
    vector<int> sz;
    vector<long long> fuel;

    struct History {
        int u, v;
        int sz_u;
        long long fuel_u;
    };
    vector<History> history;

    RollbackDSU(int n, const vector<long long>& f) {
        parent.resize(n + 1);
        sz.assign(n + 1, 1);
        fuel.resize(n + 1);
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
            fuel[i] = f[i];
        }
    }

    int find(int i) {
        while (i != parent[i]) {
            i = parent[i];
        }
        return i;
    }

    void unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);

        if (root_u == root_v) {
            return;
        }

        if (sz[root_u] < sz[root_v]) {
            swap(root_u, root_v);
        }

        history.push_back({root_u, root_v, sz[root_u], fuel[root_u]});

        parent[root_v] = root_u;
        sz[root_u] += sz[root_v];
        fuel[root_u] += fuel[root_v];
    }

    int snapshot() const {
        return history.size();
    }

    void rollback(int snapshot_size) {
        while ((int)history.size() > snapshot_size) {
            History h = history.back();
            history.pop_back();

            parent[h.v] = h.v;
            sz[h.u] = h.sz_u;
            fuel[h.u] = h.fuel_u;
        }
    }
};

const int MAXT = 100005;
vector<Edge> tree_edges[4 * MAXT];
vector<int> queries_at_time[MAXT];

void add_edge(int node, int start, int end, int l, int r, const Edge& e) {
    if (l <= start && end <= r) {
        tree_edges[node].push_back(e);
        return;
    }
    int mid = start + (end - start) / 2;
    if (l <= mid) {
        add_edge(2 * node, start, mid, l, r, e);
    }
    if (r > mid) {
        add_edge(2 * node + 1, mid + 1, end, l, r, e);
    }
}

struct Answer {
    int count;
    long long fuel;
};

void solve(int node, int start, int end, RollbackDSU& dsu, 
           const vector<Query>& queries, vector<Answer>& ans) {
    int snap = dsu.snapshot();

    for (const auto& e : tree_edges[node]) {
        dsu.unite(e.u, e.v);
    }

    if (start == end) {
        for (int q_idx : queries_at_time[start]) {
            int root = dsu.find(queries[q_idx].a);
            ans[queries[q_idx].id] = {dsu.sz[root], dsu.fuel[root]};
        }
    } else {
        int mid = start + (end - start) / 2;
        solve(2 * node, start, mid, dsu, queries, ans);
        solve(2 * node + 1, mid + 1, end, dsu, queries, ans);
    }

    dsu.rollback(snap);
}

int main() {
    // Optimize standard I/O operations
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A, K, Q;
    if (!(cin >> A >> K >> Q)) return 0;

    vector<long long> f(A + 1);
    for (int i = 1; i <= A; ++i) {
        cin >> f[i];
    }

    struct Permit {
        int u, v, s, e;
    };
    vector<Permit> permits(K);
    for (int i = 0; i < K; ++i) {
        cin >> permits[i].u >> permits[i].v >> permits[i].s >> permits[i].e;
    }

    vector<Query> queries(Q);
    vector<int> unique_times;
    unique_times.reserve(Q);

    for (int i = 0; i < Q; ++i) {
        queries[i].id = i;
        cin >> queries[i].t >> queries[i].a;
        unique_times.push_back(queries[i].t);
    }

    // Coordinate compress query times
    sort(unique_times.begin(), unique_times.end());
    unique_times.erase(unique(unique_times.begin(), unique_times.end()), unique_times.end());
    int T = unique_times.size();

    for (int i = 0; i < Q; ++i) {
        int time_idx = lower_bound(unique_times.begin(), unique_times.end(), queries[i].t) - unique_times.begin();
        queries_at_time[time_idx].push_back(i);
    }

    // Insert permits into segment tree over compressed times
    for (int i = 0; i < K; ++i) {
        int l = lower_bound(unique_times.begin(), unique_times.end(), permits[i].s) - unique_times.begin();
        int r = upper_bound(unique_times.begin(), unique_times.end(), permits[i].e) - unique_times.begin() - 1;

        if (l <= r) {
            add_edge(1, 0, T - 1, l, r, {permits[i].u, permits[i].v});
        }
    }

    RollbackDSU dsu(A, f);
    vector<Answer> ans(Q);

    solve(1, 0, T - 1, dsu, queries, ans);

    for (int i = 0; i < Q; ++i) {
        cout << ans[i].count << " " << ans[i].fuel << "\n";
    }

    return 0;
}