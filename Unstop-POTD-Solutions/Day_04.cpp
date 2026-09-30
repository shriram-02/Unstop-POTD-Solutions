#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <functional>

using namespace std;

int minimumCost(int n, int m, const vector<tuple<int, int, int>>& edges) {
    vector<int> parent(n), rank(n, 0);
    for (int i = 0; i < n; i++) parent[i] = i;

    function<int(int)> find = [&](int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    };

    auto unite = [&](int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (rank[ra] < rank[rb]) parent[ra] = rb;
        else if (rank[ra] > rank[rb]) parent[rb] = ra;
        else {
            parent[rb] = ra;
            rank[ra]++;
        }
        return true;
    };

    vector<tuple<int,int,int>> e = edges;
    sort(e.begin(), e.end(), [](auto &a, auto &b) {
        return get<2>(a) < get<2>(b);
    });

    int cost = 0, count = 0;

    for (auto &[u, v, w] : e) {
        if (unite(u, v)) {
            cost += w;
            count++;
        }
    }

    return (count == n - 1) ? cost : -1;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.emplace_back(u, v, w);
    }

    int result = minimumCost(n, m, edges);
    cout << result << endl;

    return 0;
}