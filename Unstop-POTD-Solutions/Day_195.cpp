#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_NODES = 8000005; // Sufficient node capacity for persistent segment tree
const int MAXV = 1000000;

struct Node {
    long long count;
    long long cost;
    int left, right;
};

Node tree[MAX_NODES];
int roots[200005];
int node_cnt = 0;

int update(int prev_root, int L, int R, int p, long long m, long long total_cost) {
    int curr = ++node_cnt;
    tree[curr] = tree[prev_root];
    tree[curr].count += m;
    tree[curr].cost += total_cost;
    
    if (L == R) return curr;
    
    int mid = L + (R - L) / 2;
    if (p <= mid) {
        tree[curr].left = update(tree[prev_root].left, L, mid, p, m, total_cost);
    } else {
        tree[curr].right = update(tree[prev_root].right, mid + 1, R, p, m, total_cost);
    }
    return curr;
}

pair<long long, long long> query(int u, int v, int L, int R, long long &B) {
    if (u == v) return {0, 0};
    
    long long diff_count = tree[v].count - tree[u].count;
    long long diff_cost = tree[v].cost - tree[u].cost;
    
    if (diff_cost <= B) {
        B -= diff_cost;
        return {diff_count, diff_cost};
    }
    
    if (L == R) {
        long long price = L;
        long long k = B / price;
        B -= k * price;
        return {k, k * price};
    }
    
    int mid = L + (R - L) / 2;
    int left_u = tree[u].left, left_v = tree[v].left;
    
    long long left_diff_cost = tree[left_v].cost - tree[left_u].cost;
    
    long long portions = 0, cost = 0;
    if (left_diff_cost <= B) {
        long long left_diff_count = tree[left_v].count - tree[left_u].count;
        B -= left_diff_cost;
        portions += left_diff_count;
        cost += left_diff_cost;
        
        auto right_res = query(tree[u].right, tree[v].right, mid + 1, R, B);
        portions += right_res.first;
        cost += right_res.second;
    } else {
        auto left_res = query(left_u, left_v, L, mid, B);
        portions += left_res.first;
        cost += left_res.second;
    }
    return {portions, cost};
}

int main() {
    // Optimize standard I/O operations for speed
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<long long> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }
    
    vector<long long> m(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> m[i];
    }
    
    roots[0] = 0;
    tree[0] = {0, 0, 0, 0};
    
    // Build persistent segment tree over stall updates
    for (int i = 1; i <= n; ++i) {
        roots[i] = update(roots[i - 1], 1, MAXV, p[i], m[i], m[i] * p[i]);
    }
    
    // Process queries
    for (int i = 0; i < q; ++i) {
        int l, r;
        long long B;
        cin >> l >> r >> B;
        
        long long initial_B = B;
        auto res = query(roots[l - 1], roots[r], 1, MAXV, B);
        
        // res.first = total portions tasted
        // B = remaining rupees left in the wallet
        cout << res.first << " " << B << "\n";
    }
    
    return 0;
}