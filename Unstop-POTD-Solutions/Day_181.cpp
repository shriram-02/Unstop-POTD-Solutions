#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, h;
    bool operator<(const Edge& other) const {
        return h < other.h;
    }
};

const int MAXN = 200005;

long long fund[MAXN];
int dsu_parent[MAXN];
int root_node[MAXN];
int W[MAXN];
int up[MAXN][20];
vector<int> children[MAXN];

int L_time[MAXN], R_time[MAXN];
int leaf_timer = 0;

long long bit[MAXN];
int n_leaves;

// Fenwick Tree (Binary Indexed Tree)
void add(int idx, long long val) {
    for (; idx <= n_leaves; idx += idx & -idx)
        bit[idx] += val;
}

long long query(int idx) {
    long long sum = 0;
    for (; idx > 0; idx -= idx & -idx)
        sum += bit[idx];
    return sum;
}

// Disjoint Set Union
int find_set(int v) {
    if (v == dsu_parent[v])
        return v;
    return dsu_parent[v] = find_set(dsu_parent[v]);
}

// Euler Tour DFS
void dfs(int u) {
    if (u <= n_leaves) {
        leaf_timer++;
        L_time[u] = R_time[u] = leaf_timer;
        add(leaf_timer, fund[u]);
    } else {
        L_time[u] = leaf_timer + 1;
        for (int v : children[u]) {
            dfs(v);
        }
        R_time[u] = leaf_timer;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;
    n_leaves = n;

    for (int i = 1; i <= n; i++) {
        cin >> fund[i];
        dsu_parent[i] = i;
        root_node[i] = i;
    }

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].h;
    }

    // Step 1: Sort edges to build the Kruskal Reconstruction Tree
    sort(edges.begin(), edges.end());

    int sz = n;
    for (const auto& edge : edges) {
        int rootU = find_set(edge.u);
        int rootV = find_set(edge.v);
        if (rootU != rootV) {
            sz++;
            W[sz] = edge.h;
            children[sz].push_back(root_node[rootU]);
            children[sz].push_back(root_node[rootV]);
            
            up[root_node[rootU]][0] = sz;
            up[root_node[rootV]][0] = sz;
            
            dsu_parent[rootU] = rootV;
            root_node[rootV] = sz;
            dsu_parent[sz] = sz;
            root_node[sz] = sz;
        }
    }

    // Step 2: Binary Lifting table initialization
    for (int j = 1; j < 20; j++) {
        for (int i = 1; i <= sz; i++) {
            up[i][j] = up[up[i][j - 1]][j - 1];
        }
    }

    // Step 3: DFS to linearize the tree structures
    for (int i = 1; i <= sz; i++) {
        if (up[i][0] == 0) { // Roots of the forest
            dfs(i);
        }
    }

    // Step 4: Process Queries
    for (int i = 0; i < q; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            long long v;
            cin >> x >> v;
            long long diff = v - fund[x];
            fund[x] = v;
            add(L_time[x], diff);
        } else if (type == 2) {
            int x, L;
            cin >> x >> L;
            int curr = x;
            // Jump to the highest valid ancestor
            for (int j = 19; j >= 0; j--) {
                if (up[curr][j] != 0 && W[up[curr][j]] <= L) {
                    curr = up[curr][j];
                }
            }
            long long total_fund = query(R_time[curr]) - query(L_time[curr] - 1);
            int reachable_districts = R_time[curr] - L_time[curr] + 1;
            cout << total_fund << " " << reachable_districts << "\n";
        }
    }

    return 0;
}