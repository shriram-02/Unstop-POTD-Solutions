#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Node {
    int len;
    long long l, r;
    int bi, pi, si, bd, pd, sd;
};

static Node mk(long long v) {
    Node n;
    n.len = 1; n.l = n.r = v;
    n.bi = n.pi = n.si = n.bd = n.pd = n.sd = 1;
    return n;
}

static Node mergeN(const Node &A, const Node &B) {
    if (A.len == 0) return B;
    if (B.len == 0) return A;
    Node R;
    R.len = A.len + B.len;
    R.l = A.l; R.r = B.r;
    bool up = A.r < B.l, dn = A.r > B.l;
    R.bi = max(A.bi, B.bi);
    if (up) R.bi = max(R.bi, A.si + B.pi);
    R.pi = (A.pi == A.len && up) ? A.len + B.pi : A.pi;
    R.si = (B.si == B.len && up) ? B.len + A.si : B.si;
    R.bd = max(A.bd, B.bd);
    if (dn) R.bd = max(R.bd, A.sd + B.pd);
    R.pd = (A.pd == A.len && dn) ? A.len + B.pd : A.pd;
    R.sd = (B.sd == B.len && dn) ? B.len + A.sd : B.sd;
    return R;
}

static Node revN(Node a) {
    swap(a.l, a.r);
    swap(a.bi, a.bd);
    int pi = a.pi, si = a.si, pd = a.pd, sd = a.sd;
    a.pi = sd; a.si = pd; a.pd = si; a.sd = pi;
    return a;
}

int n, q;
vector<int> adj[100005];
int par[100005], dep[100005], sz[100005], heavy[100005], head[100005], pos_[100005];
long long val[100005];
Node tr[400005];
long long base[100005];

void build(int x, int lo, int hi) {
    if (lo == hi) { tr[x] = mk(base[lo]); return; }
    int m = (lo + hi) / 2;
    build(2 * x, lo, m);
    build(2 * x + 1, m + 1, hi);
    tr[x] = mergeN(tr[2 * x], tr[2 * x + 1]);
}

void upd(int x, int lo, int hi, int p, long long v) {
    if (lo == hi) { tr[x] = mk(v); return; }
    int m = (lo + hi) / 2;
    if (p <= m) upd(2 * x, lo, m, p, v);
    else upd(2 * x + 1, m + 1, hi, p, v);
    tr[x] = mergeN(tr[2 * x], tr[2 * x + 1]);
}

Node qry(int x, int lo, int hi, int a, int b) {
    if (a <= lo && hi <= b) return tr[x];
    int m = (lo + hi) / 2;
    if (b <= m) return qry(2 * x, lo, m, a, b);
    if (a > m) return qry(2 * x + 1, m + 1, hi, a, b);
    return mergeN(qry(2 * x, lo, m, a, b), qry(2 * x + 1, m + 1, hi, a, b));
}

int main() {
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int i = 1; i <= n; i++) scanf("%lld", &val[i]);

    // iterative DFS order
    vector<int> order;
    order.reserve(n);
    vector<int> st;
    st.push_back(1);
    par[1] = 0; dep[1] = 0;
    while (!st.empty()) {
        int v = st.back(); st.pop_back();
        order.push_back(v);
        for (int w : adj[v]) {
            if (w == par[v]) continue;
            par[w] = v;
            dep[w] = dep[v] + 1;
            st.push_back(w);
        }
    }
    for (int i = 1; i <= n; i++) { sz[i] = 1; heavy[i] = 0; }
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i];
        if (par[v]) sz[par[v]] += sz[v];
    }
    for (int i = 1; i <= n; i++) {
        int best = 0;
        for (int w : adj[i]) {
            if (w == par[i]) continue;
            if (best == 0 || sz[w] > sz[best]) best = w;
        }
        heavy[i] = best;
    }
    int cur = 0;
    st.clear();
    st.push_back(1);
    while (!st.empty()) {
        int h = st.back(); st.pop_back();
        for (int v = h; v != 0; v = heavy[v]) {
            head[v] = h;
            pos_[v] = cur++;
            base[pos_[v]] = val[v];
            for (int w : adj[v]) {
                if (w == par[v] || w == heavy[v]) continue;
                st.push_back(w);
            }
        }
    }
    build(1, 0, n - 1);

    while (q--) {
        char t[3];
        int a, b;
        scanf("%s %d %d", t, &a, &b);
        if (t[0] == 'U') {
            upd(1, 0, n - 1, pos_[a], b);
        } else {
            Node L, R;
            L.len = 0; R.len = 0;
            while (head[a] != head[b]) {
                if (dep[head[a]] >= dep[head[b]]) {
                    Node s = revN(qry(1, 0, n - 1, pos_[head[a]], pos_[a]));
                    L = mergeN(L, s);
                    a = par[head[a]];
                } else {
                    Node s = qry(1, 0, n - 1, pos_[head[b]], pos_[b]);
                    R = mergeN(s, R);
                    b = par[head[b]];
                }
            }
            if (dep[a] >= dep[b]) {
                Node s = revN(qry(1, 0, n - 1, pos_[b], pos_[a]));
                L = mergeN(L, s);
            } else {
                Node s = qry(1, 0, n - 1, pos_[a], pos_[b]);
                L = mergeN(L, s);
            }
            Node res = mergeN(L, R);
            printf("%d\n", res.bi);
        }
    }
    return 0;
}