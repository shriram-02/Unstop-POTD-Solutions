#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef tree<
    pair<long long, int>,
    null_type,
    less<pair<long long, int>>,
    rb_tree_tag,
    tree_order_statistics_node_update
> ordered_set;

const int MAXN = 200005;

int parent[MAXN], sz[MAXN];
long long sum[MAXN];

int find(int x) {
    if (parent[x] != x)
        parent[x] = find(parent[x]);
    return parent[x];
}

void unite(int a, int b, ordered_set &st) {
    a = find(a);
    b = find(b);

    if (a == b) return;

    if (sz[a] < sz[b])
        swap(a, b);

    st.erase({sum[a], a});
    st.erase({sum[b], b});

    parent[b] = a;
    sz[a] += sz[b];
    sum[a] += sum[b];

    st.insert({sum[a], a});
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, C, S;
    cin >> M >> C >> S;

    for (int i = 1; i <= M; i++) {
        cin >> sum[i];
        parent[i] = i;
        sz[i] = 1;
    }

    vector<pair<int, int>> edges(C + 1);

    for (int i = 1; i <= C; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    vector<pair<int, int>> queries(S);
    vector<bool> removed(C + 1, false);

    for (int i = 0; i < S; i++) {
        int c, k;
        cin >> c >> k;
        queries[i] = {c, k};
        removed[c] = true;
    }

    ordered_set st;

    for (int i = 1; i <= M; i++) {
        st.insert({sum[i], i});
    }

    for (int i = 1; i <= C; i++) {
        if (!removed[i]) {
            unite(edges[i].first, edges[i].second, st);
        }
    }

    vector<pair<int, long long>> ans(S);

    for (int i = S - 1; i >= 0; i--) {
        int k = queries[i].second;

        int cnt = (int)st.size();
        long long capacity = 0;

        if (k <= cnt) {
            capacity = st.find_by_order(cnt - k)->first;
        }

        ans[i] = {cnt, capacity};

        int c = queries[i].first;

        unite(edges[c].first, edges[c].second, st);
    }

    for (int i = 0; i < S; i++) {
        cout << ans[i].first << " "
             << ans[i].second << "\n";
    }

    return 0;
}