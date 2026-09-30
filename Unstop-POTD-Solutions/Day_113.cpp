#include <bits/stdc++.h>
using namespace std;

using ll = long long;

class SegmentTree {
    int n;
    vector<ll> mx, lazy;

    void build(int node, int l, int r, const vector<ll>& a) {
        if (l == r) {
            mx[node] = a[l];
            return;
        }

        int mid = (l + r) / 2;
        build(node * 2, l, mid, a);
        build(node * 2 + 1, mid + 1, r, a);
        mx[node] = max(mx[node * 2], mx[node * 2 + 1]);
    }

    void push(int node) {
        if (lazy[node] != 0) {
            ll v = lazy[node];

            mx[node * 2] += v;
            mx[node * 2 + 1] += v;

            lazy[node * 2] += v;
            lazy[node * 2 + 1] += v;

            lazy[node] = 0;
        }
    }

    void update(int node, int l, int r, int ql, int qr, ll v) {
        if (qr < l || r < ql)
            return;

        if (ql <= l && r <= qr) {
            mx[node] += v;
            lazy[node] += v;
            return;
        }

        push(node);

        int mid = (l + r) / 2;
        update(node * 2, l, mid, ql, qr, v);
        update(node * 2 + 1, mid + 1, r, ql, qr, v);

        mx[node] = max(mx[node * 2], mx[node * 2 + 1]);
    }

    ll queryMax(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql)
            return LLONG_MIN;

        if (ql <= l && r <= qr)
            return mx[node];

        push(node);

        int mid = (l + r) / 2;

        return max(
            queryMax(node * 2, l, mid, ql, qr),
            queryMax(node * 2 + 1, mid + 1, r, ql, qr)
        );
    }

    int findFirst(int node, int l, int r, int ql, int qr, ll x) {
        if (r < ql || qr < l || mx[node] <= x)
            return -1;

        if (l == r)
            return l;

        push(node);

        int mid = (l + r) / 2;

        int left = findFirst(node * 2, l, mid, ql, qr, x);
        if (left != -1)
            return left;

        return findFirst(node * 2 + 1, mid + 1, r, ql, qr, x);
    }

public:
    SegmentTree(const vector<ll>& a) {
        n = a.size() - 1;
        mx.resize(4 * n + 5);
        lazy.resize(4 * n + 5);
        build(1, 1, n, a);
    }

    void update(int l, int r, ll v) {
        update(1, 1, n, l, r, v);
    }

    ll queryMax(int l, int r) {
        return queryMax(1, 1, n, l, r);
    }

    int findFirst(int l, int r, ll x) {
        return findFirst(1, 1, n, l, r, x);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<ll> a(N + 1);
    for (int i = 1; i <= N; i++)
        cin >> a[i];

    SegmentTree st(a);

    int Q;
    cin >> Q;

    while (Q--) {
        int type, l, r;
        cin >> type >> l >> r;

        if (type == 1) {
            ll v;
            cin >> v;
            st.update(l, r, v);
        }
        else if (type == 2) {
            cout << st.queryMax(l, r) << '\n';
        }
        else {
            ll x;
            cin >> x;
            cout << st.findFirst(l, r, x) << '\n';
        }
    }

    return 0;
}