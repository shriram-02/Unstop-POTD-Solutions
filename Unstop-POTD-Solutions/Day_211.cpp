
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll NEG = -(1LL << 60);

struct Node {
    ll mx[8];
    int idx[8];

    bool hasA = false;
    bool hasB = false;

    ll lazyA = 0;
    ll lazyB = 0;
};

class SegmentTree {
    int n;
    vector<Node> st;

    void pull(int p) {
        for (int mask = 0; mask < 8; mask++) {
            int L = p * 2;
            int R = L + 1;

            if (st[L].mx[mask] > st[R].mx[mask]) {
                st[p].mx[mask] = st[L].mx[mask];
                st[p].idx[mask] = st[L].idx[mask];
            }
            else if (st[L].mx[mask] < st[R].mx[mask]) {
                st[p].mx[mask] = st[R].mx[mask];
                st[p].idx[mask] = st[R].idx[mask];
            }
            else {
                st[p].mx[mask] = st[L].mx[mask];
                st[p].idx[mask] =
                    min(st[L].idx[mask], st[R].idx[mask]);
            }
        }
    }

    // Assign component A = x
    void applyA(int p, ll x) {
        for (int mask = 1; mask < 8; mask++) {
            if (mask & 1) {
                int prev = mask ^ 1;

                if (st[p].mx[prev] == NEG) {
                    st[p].mx[mask] = NEG;
                    st[p].idx[mask] = INT_MAX;
                }
                else {
                    st[p].mx[mask] = x + st[p].mx[prev];
                    st[p].idx[mask] = st[p].idx[prev];
                }
            }
        }

        st[p].hasA = true;
        st[p].lazyA = x;
    }

    // Assign component B = x
    void applyB(int p, ll x) {
        for (int mask = 1; mask < 8; mask++) {
            if (mask & 2) {
                int prev = mask ^ 2;

                if (st[p].mx[prev] == NEG) {
                    st[p].mx[mask] = NEG;
                    st[p].idx[mask] = INT_MAX;
                }
                else {
                    st[p].mx[mask] = x + st[p].mx[prev];
                    st[p].idx[mask] = st[p].idx[prev];
                }
            }
        }

        st[p].hasB = true;
        st[p].lazyB = x;
    }

    void push(int p) {
        if (st[p].hasA) {
            applyA(p * 2, st[p].lazyA);
            applyA(p * 2 + 1, st[p].lazyA);
            st[p].hasA = false;
        }

        if (st[p].hasB) {
            applyB(p * 2, st[p].lazyB);
            applyB(p * 2 + 1, st[p].lazyB);
            st[p].hasB = false;
        }
    }

    void build(int p, int l, int r) {
        for (int i = 0; i < 8; i++) {
            st[p].mx[i] = NEG;
            st[p].idx[i] = INT_MAX;
        }

        if (l == r) return;

        int mid = (l + r) / 2;

        build(p * 2, l, mid);
        build(p * 2 + 1, mid + 1, r);
    }

    void activate(int p, int l, int r,
                  int pos, ll value) {

        if (l == r) {
            for (int i = 0; i < 8; i++) {
                st[p].mx[i] = value;
                st[p].idx[i] = pos;
            }

            st[p].hasA = false;
            st[p].hasB = false;

            return;
        }

        push(p);

        int mid = (l + r) / 2;

        if (pos <= mid)
            activate(p * 2, l, mid, pos, value);
        else
            activate(p * 2 + 1, mid + 1, r, pos, value);

        pull(p);
    }

    void deactivate(int p, int l, int r, int pos) {
        if (l == r) {
            for (int i = 0; i < 8; i++) {
                st[p].mx[i] = NEG;
                st[p].idx[i] = INT_MAX;
            }

            st[p].hasA = false;
            st[p].hasB = false;

            return;
        }

        push(p);

        int mid = (l + r) / 2;

        if (pos <= mid)
            deactivate(p * 2, l, mid, pos);
        else
            deactivate(p * 2 + 1, mid + 1, r, pos);

        pull(p);
    }

    void updateA(int p, int l, int r,
                 int ql, int qr, ll x) {

        if (qr < l || r < ql) return;

        if (ql <= l && r <= qr) {
            applyA(p, x);
            return;
        }

        push(p);

        int mid = (l + r) / 2;

        updateA(p * 2, l, mid, ql, qr, x);
        updateA(p * 2 + 1, mid + 1, r, ql, qr, x);

        pull(p);
    }

    void updateB(int p, int l, int r,
                 int ql, int qr, ll x) {

        if (qr < l || r < ql) return;

        if (ql <= l && r <= qr) {
            applyB(p, x);
            return;
        }

        push(p);

        int mid = (l + r) / 2;

        updateB(p * 2, l, mid, ql, qr, x);
        updateB(p * 2 + 1, mid + 1, r, ql, qr, x);

        pull(p);
    }

public:
    SegmentTree(int n) : n(n) {
        st.resize(4 * n + 5);
        build(1, 1, n);
    }

    void activate(int pos, ll value) {
        activate(1, 1, n, pos, value);
    }

    void deactivate(int pos) {
        deactivate(1, 1, n, pos);
    }

    void updateA(int l, int r, ll x) {
        if (l <= r)
            updateA(1, 1, n, l, r, x);
    }

    void updateB(int l, int r, ll x) {
        if (l <= r)
            updateB(1, 1, n, l, r, x);
    }

    pair<ll, int> getBest() {
        return {st[1].mx[7], st[1].idx[7]};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, L;
    ll K;

    cin >> n >> L >> K;

    vector<ll> g(n + 1), t(n + 1);
    vector<ll> pref(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        cin >> g[i] >> t[i];
        pref[i] = pref[i - 1] + g[i];
    }

    SegmentTree seg(n);

    // Monotonic stacks
    vector<int> stMax, stMin;

    ll bestScore = NEG;
    int bestLeft = -1;
    int bestRight = -1;

    for (int r = 1; r <= n; r++) {

        // Activate the new starting position.
        // A = 0, B = 0, C = -pref[r-1].
        seg.activate(r, -pref[r - 1]);

        // Update maximum turbulence.
        while (!stMax.empty() &&
               t[stMax.back()] < t[r]) {
            stMax.pop_back();
        }

        int pMax = stMax.empty() ? 0 : stMax.back();

        // All starts in [pMax+1, r]
        // now have maximum turbulence t[r].
        seg.updateA(pMax + 1, r, -K * t[r]);

        stMax.push_back(r);

        // Update minimum turbulence.
        while (!stMin.empty() &&
               t[stMin.back()] > t[r]) {
            stMin.pop_back();
        }

        int pMin = stMin.empty() ? 0 : stMin.back();

        // All starts in [pMin+1, r]
        // now have minimum turbulence t[r].
        seg.updateB(pMin + 1, r, K * t[r]);

        stMin.push_back(r);

        // Enforce maximum campaign length L.
        int expired = r - L;

        if (expired >= 1) {
            seg.deactivate(expired);
        }

        // Find the best starting position for this r.
        auto [value, left] = seg.getBest();

        ll currentScore = pref[r] + value;

        // Iterating r from left to right automatically
        // resolves ties by smaller right endpoint.
        // Segment tree resolves ties by smaller left endpoint.
        if (currentScore > bestScore) {
            bestScore = currentScore;
            bestLeft = left;
            bestRight = r;
        }
    }

    cout << bestScore << '\n';
    cout << bestLeft << " " << bestRight << '\n';

    return 0;
}