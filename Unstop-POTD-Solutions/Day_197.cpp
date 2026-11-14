
#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
    int n;
    vector<int> tree;

public:
    SegmentTree(int n) : n(n) {
        tree.assign(4 * n, 0);
    }

    void build(int node, int start, int end, string &s) {
        if (start == end) {
            tree[node] = (s[start - 1] == '.') ? 1 : 0;
            return;
        }

        int mid = (start + end) / 2;
        build(node * 2, start, mid, s);
        build(node * 2 + 1, mid + 1, end, s);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    void update(int node, int start, int end, int pos, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }

        int mid = (start + end) / 2;

        if (pos <= mid)
            update(node * 2, start, mid, pos, val);
        else
            update(node * 2 + 1, mid + 1, end, pos, val);

        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l)
            return 0;

        if (l <= start && end <= r)
            return tree[node];

        int mid = (start + end) / 2;

        return query(node * 2, start, mid, l, r) +
               query(node * 2 + 1, mid + 1, end, l, r);
    }

    int findFirst(int node, int start, int end, int l) {
        if (end < l || tree[node] == 0)
            return -1;

        if (start == end)
            return start;

        int mid = (start + end) / 2;

        int ans = findFirst(node * 2, start, mid, l);

        if (ans == -1)
            ans = findFirst(node * 2 + 1, mid + 1, end, l);

        return ans;
    }

    int getFirst(int l) {
        return findFirst(1, 1, n, l);
    }

    void setPosition(int pos, int val) {
        update(1, 1, n, pos, val);
    }

    int total() {
        return tree[1];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    string s;
    cin >> s;

    SegmentTree st(N);
    st.build(1, 1, N, s);

    vector<int> bookings;
    vector<bool> withdrawn;

    for (int i = 0; i < Q; i++) {
        int x;
        cin >> x;

        if (x > 0) {
            int pos = -1;

            if (st.total() > 0) {
                pos = st.getFirst(x);

                if (pos == -1)
                    pos = st.getFirst(1);
            }

            bookings.push_back(pos);
            withdrawn.push_back(false);

            if (pos != -1)
                st.setPosition(pos, 0);

        } else {
            int j = -x;

            if (j <= (int)bookings.size() &&
                bookings[j - 1] != -1 &&
                !withdrawn[j - 1]) {

                st.setPosition(bookings[j - 1], 1);
                withdrawn[j - 1] = true;
            }
        }
    }

    for (int i = 0; i < (int)bookings.size(); i++) {
        if (i) cout << " ";
        cout << (bookings[i] == -1 ? 0 : bookings[i]);
    }

    cout << '\n';

    return 0;
}
