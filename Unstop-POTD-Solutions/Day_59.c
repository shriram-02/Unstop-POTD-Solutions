#include <stdio.h>
#include <string.h>

#define MAXN 100005

typedef struct {
    int to, next;
} Edge;

Edge E[2 * MAXN];
int head[MAXN], ecnt;

int parent_[MAXN], depth_[MAXN];
int heavy[MAXN], sz[MAXN];

int chainHead[MAXN];
int pos[MAXN];
int curPos;

typedef struct {
    int sum;
    int lazy;
} SegNode;

SegNode seg[4 * MAXN];

void addEdge(int u, int v) {
    E[ecnt].to = v;
    E[ecnt].next = head[u];
    head[u] = ecnt++;

    E[ecnt].to = u;
    E[ecnt].next = head[v];
    head[v] = ecnt++;
}

void dfs(int u, int p) {
    parent_[u] = p;
    sz[u] = 1;
    heavy[u] = -1;

    int maxSub = 0;

    for (int e = head[u]; e != -1; e = E[e].next) {
        int v = E[e].to;
        if (v == p) continue;

        depth_[v] = depth_[u] + 1;
        dfs(v, u);

        sz[u] += sz[v];

        if (sz[v] > maxSub) {
            maxSub = sz[v];
            heavy[u] = v;
        }
    }
}

void decompose(int u, int h) {
    chainHead[u] = h;
    pos[u] = ++curPos;

    if (heavy[u] != -1)
        decompose(heavy[u], h);

    for (int e = head[u]; e != -1; e = E[e].next) {
        int v = E[e].to;
        if (v == parent_[u] || v == heavy[u]) continue;
        decompose(v, v);
    }
}

void apply(int idx, int l, int r) {
    seg[idx].sum = (r - l + 1) - seg[idx].sum;
    seg[idx].lazy ^= 1;
}

void push(int idx, int l, int r) {
    if (!seg[idx].lazy || l == r) return;

    int mid = (l + r) >> 1;

    apply(idx << 1, l, mid);
    apply(idx << 1 | 1, mid + 1, r);

    seg[idx].lazy = 0;
}

void update(int idx, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return;

    if (ql <= l && r <= qr) {
        apply(idx, l, r);
        return;
    }

    push(idx, l, r);

    int mid = (l + r) >> 1;

    update(idx << 1, l, mid, ql, qr);
    update(idx << 1 | 1, mid + 1, r, ql, qr);

    seg[idx].sum =
        seg[idx << 1].sum +
        seg[idx << 1 | 1].sum;
}

int querySeg(int idx, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;

    if (ql <= l && r <= qr)
        return seg[idx].sum;

    push(idx, l, r);

    int mid = (l + r) >> 1;

    return querySeg(idx << 1, l, mid, ql, qr) +
           querySeg(idx << 1 | 1, mid + 1, r, ql, qr);
}

/* Edge represented by child node position.
   Root position does not correspond to an edge. */

void pathUpdate(int u, int v, int n) {
    while (chainHead[u] != chainHead[v]) {
        if (depth_[chainHead[u]] < depth_[chainHead[v]]) {
            int t = u; u = v; v = t;
        }

        update(
            1, 1, n,
            pos[chainHead[u]],
            pos[u]
        );

        u = parent_[chainHead[u]];
    }

    if (depth_[u] > depth_[v]) {
        int t = u; u = v; v = t;
    }

    if (u != v)
        update(1, 1, n, pos[u] + 1, pos[v]);
}

int pathQuery(int u, int v, int n) {
    int ans = 0;

    while (chainHead[u] != chainHead[v]) {
        if (depth_[chainHead[u]] < depth_[chainHead[v]]) {
            int t = u; u = v; v = t;
        }

        ans += querySeg(
            1, 1, n,
            pos[chainHead[u]],
            pos[u]
        );

        u = parent_[chainHead[u]];
    }

    if (depth_[u] > depth_[v]) {
        int t = u; u = v; v = t;
    }

    if (u != v)
        ans += querySeg(
            1, 1, n,
            pos[u] + 1,
            pos[v]
        );

    return ans;
}

void process_queries(int n, int edges[][2], int q, int queries[][3]) {
    memset(head, -1, sizeof(head));
    ecnt = 0;

    for (int i = 0; i < n - 1; i++) {
        addEdge(edges[i][0], edges[i][1]);
    }

    depth_[1] = 0;
    dfs(1, 0);

    curPos = 0;
    decompose(1, 1);

    for (int i = 0; i < q; i++) {
        int type = queries[i][0];
        int u = queries[i][1];
        int v = queries[i][2];

        if (type == 1) {
            pathUpdate(u, v, n);
        } else {
            printf("%d\n", pathQuery(u, v, n));
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);

    int edges[n - 1][2];
    for (int i = 0; i < n - 1; i++) {
        scanf("%d %d", &edges[i][0], &edges[i][1]);
    }

    int q;
    scanf("%d", &q);

    int queries[q][3];
    for (int i = 0; i < q; i++) {
        scanf("%d %d %d",
              &queries[i][0],
              &queries[i][1],
              &queries[i][2]);
    }

    process_queries(n, edges, q, queries);

    return 0;
}